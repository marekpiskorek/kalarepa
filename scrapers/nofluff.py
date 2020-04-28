import json
import os

import requests

OUTPUT_FILENAME = os.environ["FILEPATH"]

URL_WARSAW = "https://nofluffjobs.com/api/search/posting?criteria=python+city%3Dwarszawa+category%3Dbackend"
URL_REMOTE = "https://nofluffjobs.com/api/search/posting?criteria=python+remote%3D100+category%3Dbackend"

# FIXME: NoFluff has changed its whole web design and moved to more elaborate, JS-based solutions for fetching the data.
#        It'll reqiure more work to be performed on this one.


class NoFluffScrapper:
    def __init__(self, filename=None):
        self.filename = OUTPUT_FILENAME if filename is None else filename
        with open(self.filename, "rb") as jfile:
            self.json_data = json.load(jfile)

    def get_data_from_nofluff(self):
        self.headers = {
            "content-type": "application/json, text/plain",
            "User-Agent": (
                "Mozilla/5.0 (X11; Linux x86_64; rv:57.0) "
                "Gecko/20100101 Firefox/57.0"
            ),
            "Host": "noflufjobs.com",
            "Referer": "https://nofluffjobs.com",
        }
        for url in (URL_REMOTE, URL_WARSAW):
            response = requests.get(url, headers=self.headers)
            self._prepare_jobs_dict(response)
        with open(self.filename, "w") as json_file:
            json.dump(self.json_data, json_file)

    def _prepare_jobs_dict(self, response):
        for brief_data in response.json().get("postings", []):
            detailed_url = f'https://nofluffjobs.com/api/posting/{brief_data["id"]}'
            # TODO: change below to session request in order to reduce headers
            response = requests.get(detailed_url, headers=self.headers)
            url = f'https://nofluffjobs.com/job/{brief_data["id"]}'
            offer = response.json().get("posting")
            print(f'Scrapping offer {brief_data["title"]}')
            if self.json_data.get(url) is not None:
                print(f"Duplicated url: {url}")
                continue
            self.json_data[url] = offer
