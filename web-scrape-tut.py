#basic web scraper, based on tutorial at http://first-web-scraper.readthedocs.org/en/latest/

import requests
from BeautifulSoup import BeautifulSoup
import csv

url = 'https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('tbody', attrs={'id': 'mrc_main_table'})

rowList = []
for row in table.findAll('tr'):
	cellList = []
	for cell in row.findAll('td'):
		text = cell.text.replace('&nbsp;','')
		cellList.append(text)
	rowList.append(cellList)

outfile = open("./inmates.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["Last", "First", "Middle", "Gender", "Race", "Age", "City", "State"])
writer.writerows(rowList)