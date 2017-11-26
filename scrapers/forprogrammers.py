from bs4 import BeautifulSoup
from pprint import pprint
import requests


def get_offers_from_forprogrammers():
    response = requests.get(
        'https://4programmers.net/Praca?q=Python&city=Warszawa'
    )
    soup = BeautifulSoup(response.content, 'html.parser')
    links = [f.get('href') for f in soup.find_all('a')]
    # TODO: change hard-coded '3' onto an integer 'regex'
    job_prefix = 'https://4programmers.net/Praca/3'
    job_links = [
        link for link in links
        if isinstance(link, str) and link.startswith(job_prefix)
    ]
    for job_link in job_links:
        get_offer_details(job_link)
        break


def get_offer_details(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.content, 'html.parser')
    job_title = soup.find(attrs={'class': 'media-heading'}).text
    employer = soup.find(attrs={'class': 'employer'}).text
    # TODO: handle each part of payment separately
    payment = soup.find(attrs={'class': 'salary pull-right'}).text.replace('\n    \n', '\t').replace(' ', '').replace('\n', '').replace('\t', ' ')
    details = {detail.find('small').text: detail.find('strong').text for detail in soup.find(attrs={'class': 'about-items'}).children if len(detail) > 2}
    import ipdb; ipdb.set_trace()
    assert 1 == 1
