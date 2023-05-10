#!/usr/bin/env

from urllib.parse import urlparse, urljoin, urlunparse
import sys
import os

sys.path.append('../..')


# API endpoint.
url = urlparse(os.environ.get('API_SIXT'))

print(url)
# # Generate all resquest urls based on dates and pickup station.
# def generate_url_yearly():
#     urls = []
#     for chunk in get_days_groups_yearly_from_now(3):
#         chunk = [d.strftime("%Y-%m-%dT%H:%M:%S") for d in chunk]
#         query = [f"pickupDate={chunk[0]}&returnDate={chunk[-1]}"]
#         request_url = url._replace(query=query[0])
#         urls.append(urlunparse(request_url))
#     return urls

# print(urls)
 