import requests
import pendulum
import aiohttp
from urllib.parse import urlparse, urlencode, parse_qs

# Internal imports
from src.utils.dates import get_days_groups_yearly_from_now
from src.utils.fetch import fetch_all

# Base URL
base_url="https://web-api.orange.sixt.com/v1/rentaloffers/offers?pickupStation=S_40106&returnStation=S_40106&pickupDate=2023-02-17T17:00:00&returnDate=2023-02-20T17:00:00&vehicleType=car&currency=EUR&isoCountryCode=FR"

# Parse the base URL
url_parts = urlparse(base_url)
query_params = parse_qs(url_parts.query)

# Get All stations list
def stations_list():
   stations = [str("S_")+ str(i).zfill(5) for i in range(0, 99999, 10)]
   results = [{'id': i, 'city': 'Nanterre'} for i in stations]
   return results
   
# Generate URL for a givent number of days.
def generate_url_yearly(days: int):
    urls = []
    for day in get_days_groups_yearly_from_now(days):
        day = [d.strftime("%Y-%m-%dT%H:%M:%S") for d in day] # Convert datetime to string
        query_params['pickupDate'] = day[0]
        query_params['returnDate'] = day[-1]
        item = url_parts._replace(query=urlencode(query_params, doseq=True)).geturl()
        urls.append(item)
    return urls


# Fetch all urls from a list
async def get_bulk_results(days: int = 3):
    urls = generate_url_yearly(days)[0:5]
    async with aiohttp.ClientSession() as session:
        results = await fetch_all(session, urls)
        return results


# Get finals results
def compare_results(days: int = 3):
   # Fetch results for the second item of the url list generate_url_yearly(3)[1]
   response = requests.get(generate_url_yearly(days)[2])
   data = response.json()
   
   pickupDate = pendulum.parse(data['info']['pickupDate'], tz="Europe/Paris")
   returnDate = pendulum.parse(data['info']['returnDate'], tz="Europe/Paris")
   duration = returnDate - pickupDate

   infos = {
         'Location': "Rueil-Malmaison/Nanterre",
         'pickupStation': data['info']['pickupStationId'],
         'returnStation': data['info']['returnStationId'],
         'pickupDate': pickupDate,
         'returnDate': returnDate,
         'pickupDateHuman': pickupDate.format("dddd Do [of] MMMM YYYY HH:mm:ss A"),
        #  'returnDateHuman': returnDate.format("dddd Do [of] MMMM YYYY HH:mm:ss A"),
         'days': duration.days,
         'link': "www.sixt.com"
   }
   # Generate a list of offers of one url and put 
   offers = []
   for offer in data['offers']:
       offers.append({
           'id': offer['id'], 
           'status': offer['status'], 
           'description': offer['description'],
           'maxDistance': offer['mileageInfo']['display'],
           'maxPassengers': offer['vehicleGroupInfo']['maxPassengers'],
           'dayPrice': offer['prices']['dayPrice']['amount']["value"],
           'basePrice': offer['prices']['totalPrice']['amount']["value"],
           })
    
   # Return the list of offers sorted by dayPrice
   return {
       'infos': infos,
       'offers': sorted(offers, key=lambda k: k['dayPrice'])
       }