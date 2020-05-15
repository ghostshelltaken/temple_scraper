import requests
from bs4 import BeautifulSoup


def soupObj(URL):

	result = requests.get(URL)

	soup = BeautifulSoup(result.content, 'lxml')

	return soup