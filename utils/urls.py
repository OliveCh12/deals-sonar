from urllib.parse import urlparse, urljoin, urlunparse
from pprint import pprint
from dates import get_days_groups_yearly_from_now

url = urlparse("https://web-api.orange.sixt.com/v1/rentaloffers/offers?pickupStation=S_40106&returnStation=S_40106&pickupDate=2023-02-17T17:00:00&returnDate=2023-02-20T17:00:00&vehicleType=car&currency=EUR&isoCountryCode=FR")


# Replace the date time.
new_url = url._replace(query="pickupDate=2024-02-17T17:00:00&returnDate=2023-02-20T17:00:00")
new_url = url._replace(query="")


# Generate all resquest urls based on dates and pickup station and return station.
for chunk in get_days_groups_yearly_from_now(3):
    chunk = [d.strftime("%Y-%m-%dT%H:%M:%S") for d in chunk]
    query = [f"pickupDate={chunk[0]}&returnDate={chunk[-1]}"]
    request_url = url._replace(query=query[0])
    print(urlunparse(request_url))

# def get_urls_list():
#     urls_list = []
#     for date in get_days_groups_yearly_from_now(10):
#         dt = [d.strftime("%Y-%m-%dT%H:%M:%S") for d in date]
#         url._replace(query=f"pickupDate={dt[0]}&returnDate={dt[-1]}")
#         urls_list.append(urljoin(url))
#     return urls_list
