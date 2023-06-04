import requests
import pendulum
from urllib.parse import urlparse, urlencode, parse_qs
from api.utils.dates import get_days_groups_yearly_from_now

# Base URL
base_url="https://web-api.orange.sixt.com/v1/rentaloffers/offers?pickupStation=S_40106&returnStation=S_40106&pickupDate=2023-02-17T17:00:00&returnDate=2023-02-20T17:00:00&vehicleType=car&currency=EUR&isoCountryCode=FR"

# Parse the base URL
url_parts = urlparse(base_url)
query_params = parse_qs(url_parts.query)

# Get All stations list
def stations_list(): 
#    station = "S_40106"
   response = requests.get(generate_url_yearly(3)[2])
   data = response.json()
   data = data['offers'][0]
   stations = [str("S_")+ str(i).zfill(5) for i in range(0, 99999)]
   stations_length = len(stations)
   return data
   
# Generate URL for a givent number of days.
def generate_url_yearly(days: int):
    urls = []
    for day in get_days_groups_yearly_from_now(days):
        day = [d.strftime("%Y-%m-%dT%H:%M:%S") for d in day] # Convert datetime to string
        query_params['pickupDate'] = day[0] # Pickup date
        query_params['returnDate'] = day[-1] # Return date
        item = url_parts._replace(query=urlencode(query_params, doseq=True)).geturl()
        urls.append(item)
    return urls


# Get finals results
def compare_results(days: int = 3):
   # Fetch results for the second item of the url list generate_url_yearly(3)[1]
   response = requests.get(generate_url_yearly(days)[2])
   data = response.json()
   
#    print(generate_url_yearly(days)[2])
   # Get pendulum date from data['info']['pickupDate'] and data['info']['returnDate']
   pickupDate = pendulum.parse(data['info']['pickupDate'])
   returnDate = pendulum.parse(data['info']['returnDate'])
   infos = {
         'Location': "Rueil-Malmaison/Nanterre",
         'pickupStation': data['info']['pickupStationId'],
         'returnStation': data['info']['returnStationId'],
         'pickupDate': pickupDate,
         'returnDate': returnDate,
         'duration': pickupDate.diff_for_humans(returnDate, absolute=True),
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