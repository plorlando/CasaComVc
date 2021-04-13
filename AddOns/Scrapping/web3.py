import parts as parts
from bs4 import BeautifulSoup
import requests
import requests.exceptions
from urllib.parse import urlsplit
from urllib.parse import urlparse
from collections import deque

url = 'https://scrapethissite.com'

# a queue of urls to be crawled next
new_urls = deque([url])

# a set of urls that we have already processed
processed_urls = set()

# a set of domains inside the target website
local_urls = set()

# a set of domains outside the target website
foreign_urls = set()

# a set of broken urls
broken_urls = set()

# process urls one by one until we exhaust the queue
while len(new_urls):
    # move url from the queue to processed url set
    url = new_urls.popleft()
    processed_urls.add(url)
    # print the current url
    print('Processing %s' % url)

    try:
        response = requests.get(url)
    except(requests.exceptions.MissingSchema, requests.exceptions.ConnectionError, requests.exceptions.InvalidURL, requests.exceptions.InvalidSchema):
        # add broken urls to it’s own set, then continue
        broken_urls.add(url)
    continue

# extract base url to resolve relative
linksparts = urlsplit(url)
base = '{0.netloc}'.format(parts)
strip_base = base.replace('www.', '')
base_url = '{0.scheme}://{0.netloc}'.format(parts)
path = url[:url.rfind('/')+1] if '/' in parts.path else url