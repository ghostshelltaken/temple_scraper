from soupObj import soupObj
from bs4 import BeautifulSoup
from db_manage import Database

rawURL = 'https://www.ixigo.com'

def get_temple_links():
	'''
	This function returns all the links of the temples
	'''
	temple_links = []

	with open('./assests/links.html', 'r') as f:

		soup = BeautifulSoup (f, 'lxml')

		links = soup.select('div.namedentity-item.row div.namedentity-info div.ne-title a')
		# print(links)
		for item in links:

			temple_links.append(item['href'])

	return temple_links



def get_temple_details(templeLinks):

	for link in templeLinks:

		URL = rawURL + link

		soup = soupObj(URL)

		temple_name = soup.select('div.section-description h2.title.sec-header span.city-name.poi-title')[0].getText()
		print(temple_name)

		try:
			rating = soup.select('div.ne-info div.rating-value')[0].getText()
		except:
			rating = None

		try:
			visit_duration = soup.select('div.visit-duration-container div.duration')[0].getText().strip()
		except:
			visit_duration = None

		try:
			address = soup.select('div.lfloat.info-address.info-subsection div.threerow-div span')[0].getText()
		except:
			address = None

		

	




def main():
	'''
	So There is a show more button on the website so could not get it without selenium.
	I copied code of that and put that into abc.html file and will read it from it.
	'''

	templeLinks = get_temple_links()
	
	get_temple_details(templeLinks)

if __name__ == '__main__':
	main()