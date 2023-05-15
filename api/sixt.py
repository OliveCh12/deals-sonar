#!/usr/bin/env

from urllib.parse import urlparse, urlencode, parse_qs
from pprint import pprint
from utils.dates import get_days_groups_yearly_from_now

# Base URL
base_url="https://web-api.orange.sixt.com/v1/rentaloffers/offers?pickupStation=S_40106&returnStation=S_40106&pickupDate=2023-02-17T17:00:00&returnDate=2023-02-20T17:00:00&vehicleType=car&currency=EUR&isoCountryCode=FR"

# Parse the base URL
url_parts = urlparse(base_url)
query_params = parse_qs(url_parts.query)

# # Modify the query parameters
# query_params['pickupStation'] = 'S_40106'
# query_params['returnStation'] = 'S_40106'
# query_params['pickupDate'] = '2023-05-20T10:00:00'
# query_params['returnDate'] = '2023-05-23T10:00:00'

# url_parts = url_parts._replace(query=urlencode(query_params, doseq=True))
# modified_url = url_parts.geturl()


def generate_url_yearly(days: int):
    urls = []
    for day in get_days_groups_yearly_from_now(days):
        day = [d.strftime("%Y-%m-%dT%H:%M:%S") for d in day] # Convert datetime to string
        query_params['pickupDate'] = day[0] # Pickup date
        query_params['returnDate'] = day[-1] # Return date
        item = url_parts._replace(query=urlencode(query_params, doseq=True)).geturl()
        urls.append(item)
    return urls

pprint(generate_url_yearly(2))
 