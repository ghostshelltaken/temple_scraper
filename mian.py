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
	'''
	This function crawls throught one by one to each temple and gathers details of each one.
	'''
	for link in templeLinks:

		dbObj = Database()

		URL = rawURL + link

		soup = soupObj(URL)

		temple_name = soup.select('div.section-description h2.title.sec-header span.city-name.poi-title')[0].getText()
		# print(temple_name)

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

		try:
			contat = soup.select('div.lfloat.info-contact.info-subsection div.threerow-div span')[0].getText()
		except:
			contat = None

		try:
			knwn_for = soup.select('div.popular-for-container div.who')
		except:
			knwn_for = None

		popular_for = []

		if knwn_for:
			for i in knwn_for:
				popular_for.append(i.getText().strip())
		else:
			popular_for = None

		query = "INSERT into temple_details(temple_name, ratings, visit_durations, Address) values(?, ?, ?, ?)", (temple_name, rating, visit_duration, address)

		dbObj.make_connection()
		dbObj.execute_query(query)
		dbObj.close_connection()

		query = 'SELECT temple_id FROM temple_details WHERE temple_name = ? ORDER by temple_id DESC ', (temple_name, )

		dbObj.make_connection()
		data = dbObj.select_query(query)
		dbObj.close_connection()
		print(data)
		temple_id = data[0][0]

		query = "INSERT INTO contacts(temple_id, contact_no) VALUES(?, ?)", (temple_id, contat)

		dbObj.make_connection()
		dbObj.execute_query(query)
		dbObj.close_connection()

		if popular_for == None:
			query = "INSERT INTO known_for(temple_id, popular_for) VALUES(?, ?)", (temple_id, popular_for)	

			dbObj.make_connection()
			dbObj.execute_query(query)
			dbObj.close_connection()			

		else:
			for i in range(len(popular_for)):
				query = "INSERT INTO known_for(temple_id, popular_for) VALUES(?, ?)", (temple_id, popular_for[i])	

				dbObj.make_connection()
				dbObj.execute_query(query)
				dbObj.close_connection()

		print(f"Scraped Data for {temple_name}")



def main():
	'''
	So There is a show more button on the website so could not get it without selenium.
	I copied code of that and put that into abc.html file and will read it from it.
	'''

	templeLinks = get_temple_links()
	
	get_temple_details(templeLinks)

if __name__ == '__main__':
	main()