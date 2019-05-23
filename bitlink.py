import requests
import re
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ['BITLY_TOKEN']

BASE_URL = 'https://api-ssl.bitly.com/v4/{}'
CREATE_URL = BASE_URL.format('bitlinks')
STATS_URL = BASE_URL.format('bitlinks/{}/clicks')
CHECK_URL = BASE_URL.format('bitlinks/{}')


def get_headers():
    return {
        'Authorization': 'Bearer {}'.format(TOKEN),
        'Content-Type': 'application/json'
      }


def process_url(url):
    if is_bitlink(url):
        return get_url_stats(url)
    else:
        return create_url(url)


def create_url(url):
    payload = {
      'long_url': url,
    }

    response = requests.post(CREATE_URL, json=payload, headers=get_headers())

    if response.ok:
        return response.json()['link']
    else:
        return None


def get_url_stats(url):
    payload = {
      'unit': 'day',
      'units': -1
    }

    url = STATS_URL.format(prepare_url(url))

    response = requests.get(url, json=payload, headers=get_headers())

    if not response.ok:
        return None

    return response.json()


def is_bitlink(url):
    url = CHECK_URL.format(prepare_url(url))

    return requests.get(url, headers=get_headers()).ok


def prepare_url(url):
    return re.sub('https?://', '', url)
