import json

import requests

from .settings import OUTPUT_FILENAME


def get_all_offers_from_justjoinit():
    """ API call doesn't seem to respect any filters, we may need to filter
    offers manually in JSON / Mongo. """
    url = 'https://justjoin.it/api/offers'

    headers = {
        'content-type': 'application/json, text/plain',
        'User-Agent': (
            'Mozilla/5.0 (X11; Linux x86_64; rv:57.0) '
            'Gecko/20100101 Firefox/57.0'
        ),
        'Host': 'justjoin.it',
        'Referer': 'justjoin.it',
    }
    response = requests.get(url, headers=headers)
    jobs_dict = _prepare_jobs_dict(response)
    with open(OUTPUT_FILENAME, 'w') as json_file:
        json.dump(jobs_dict, json_file)

def _prepare_jobs_dict(response):
    with open(OUTPUT_FILENAME, 'r') as json_file:
        jobs_dict  = json.load(json_file)
    for offer_dict in response.json():
        url = f'https://justjoin.it/offers/{offer_dict["id"]}'
        if offer_dict.get('marker_icon') != 'python':
            print(f'Not a Python link: {url}')
            continue
        if jobs_dict.get(url) is not None:
            print(f'Duplicated url: {url}')
            continue
        jobs_dict[url] = offer_dict
    return jobs_dict
