from bs4 import BeautifulSoup
from pprint import pprint
import requests


def get_offers_from_4programmers():
    response = requests.get(
        'https://4programmers.net/Praca?q=Python&city=Warszawa'
    )
    soup = BeautifulSoup(response.content, 'html.parser')
    links = [f.get('href') for f in soup.find_all('a')]
    job_prefix = 'https://4programmers.net/Praca/3'
    job_links = [link for link in links if link.startswith(job_prefix)]
    pprint(job_links)


if __name__ == '__main__':
    get_offers_from_4programmers()
