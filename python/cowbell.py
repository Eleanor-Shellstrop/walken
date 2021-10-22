from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv



songs = []


def main(start, end):
	id = 1
	while id >= start and id <= end:
		user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.37"
		URL = f"http://ultimatecowbell.com/songview.php?idsongperm={id}"
		response = requests.get(URL, headers={'User-Agent': user_agent})
		html = response.content
		soup = BeautifulSoup(html, "lxml")
		song = []
		for b in soup.find_all('b'):
			if len(soup.find_all('b')) == 5:
				song.append(b.get_text(strip=True))
		songs.append(song)
		id = id + 1
	# Add data scraped into a dataframe 
	df = pd.DataFrame(songs, columns = ['Band', 'Song', 'Album', 'Record_Company', 'Year']) 
	df.to_csv(f'cowbell{start}_{end}.csv', sep=',', encoding='utf-8-sig', index = False)


main(1, 4247)