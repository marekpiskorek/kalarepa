from pprint import pprint
import requests


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
    pprint(response.json())
