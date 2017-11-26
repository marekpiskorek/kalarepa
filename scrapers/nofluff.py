from pprint import pprint
import requests


def get_data_from_nofluff():
    url = (
        'https://nofluffjobs.com/api/search/posting'
        '?criteria=python+city%3Dwarszawa+category%3Dbackend'
    )
    headers = {
        'content-type': 'application/json, text/plain',
        'User-Agent': (
            'Mozilla/5.0 (X11; Linux x86_64; rv:57.0) '
            'Gecko/20100101 Firefox/57.0'
        ),
        'Host': 'noflufjobs.com',
        'Referer': 'https://nofluffjobs.com',
    }
    response = requests.get(url, headers=headers)
    pprint(response.json())
