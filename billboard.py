from bs4 import BeautifulSoup
import requests
import pandas as pd
import pprint



bbsongs = []


ids = ['1970s', '1980s']


for id in ids:
	user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.37"
	URL = f"https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number-one_singles_of_the_{id}"
	response = requests.get(URL, headers={'User-Agent': user_agent})
	html = response.content
	soup = BeautifulSoup(html, "lxml")
	song = []
	for tr in soup.find_all('tr'):
		data = []
		for td in tr:
			if '\n' in td.text:
				continue
			data.append(td.get_text())
		if (data == []) or (len(data) < 5):
			continue
		song.append(data)
	bbsongs.append(song)
# Add data scraped into a dataframe 
#df = pd.DataFrame(bbsongs, columns = ['Band', 'Song', 'Album', 'Record_Company', 'Year']) 
#df.to_csv(f'cowbell{start}_{end}.csv', sep=',', encoding='utf-8-sig', index = False)

pprint.pprint(bbsongs)