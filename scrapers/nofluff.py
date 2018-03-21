import json

import requests

from settings import OUTPUT_FILENAME


class NoFluffScrapper:

    def __init__(self, filename=None):
        if filename is None:
            self.filename = OUTPUT_FILENAME
        with open(self.filename, 'rb') as jfile:
            self.json_data = json.load(jfile)

    def get_data_from_nofluff(self):
        url = (
            'https://nofluffjobs.com/api/search/posting'
            '?criteria=python+city%3Dwarszawa+category%3Dbackend'
        )
        self.headers = {
            'content-type': 'application/json, text/plain',
            'User-Agent': (
                'Mozilla/5.0 (X11; Linux x86_64; rv:57.0) '
                'Gecko/20100101 Firefox/57.0'
            ),
            'Host': 'noflufjobs.com',
            'Referer': 'https://nofluffjobs.com',
        }
        response = requests.get(url, headers=self.headers)
        self._prepare_jobs_dict(response)
        with open(self.filename, 'w') as json_file:
            json.dump(self.json_data, json_file)

    def _prepare_jobs_dict(self, response):
        for brief_data in response.json().get('postings', []):
            detailed_url = (
                f'https://nofluffjobs.com/api/postingNew/{brief_data["id"]}'
            )
            # TODO: change below to session request in order to reduce headers
            response = requests.get(detailed_url, headers=self.headers)
            url = f'https://nofluffjobs.com/job/{brief_data["id"]}'
            offer = response.json().get('posting')
            print(f'Scrapping offer {brief_data["title"]}')
            if self.json_data.get(url) is not None:
                print(f'Duplicated url: {url}')
                continue
            self.json_data[url] = offer
