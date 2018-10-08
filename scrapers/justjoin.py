import json
import os

import requests

OUTPUT_FILENAME = os.environ["FILEPATH"]


class JustJoinScrapper:
    def __init__(self, filename=None):
        if filename is None:
            self.filename = OUTPUT_FILENAME
        with open(self.filename, "rb") as jfile:
            self.json_data = json.load(jfile)

    def get_all_offers_from_justjoinit(self):
        """ API call doesn't seem to respect any filters, we may need to filter
        offers manually in JSON / Mongo. """
        url = "https://justjoin.it/api/offers"

        headers = {
            "content-type": "application/json, text/plain",
            "User-Agent": (
                "Mozilla/5.0 (X11; Linux x86_64; rv:57.0) "
                "Gecko/20100101 Firefox/57.0"
            ),
            "Host": "justjoin.it",
            "Referer": "justjoin.it",
        }
        response = requests.get(url, headers=headers)
        self._prepare_jobs_dict(response)
        with open(self.filename, "w") as json_file:
            json.dump(self.json_data, json_file)

    def _prepare_jobs_dict(self, response):
        for offer_dict in response.json():
            url = f'https://justjoin.it/offers/{offer_dict["id"]}'
            if offer_dict.get("marker_icon") != "python":
                print(f"Not a Python link: {url}")
                continue
            if offer_dict.get("city") not in (
                "Warsaw",
                "Warszawa",
            ) or not offer_dict.get("remote"):
                print(f"Not a Warsaw located or remote offer: {url}")
                continue
            if self.json_data.get(url) is not None:
                print(f"Duplicated url: {url}")
                continue
            self.json_data[url] = offer_dict
