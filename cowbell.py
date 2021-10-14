from bs4 import BeautifulSoup
import requests



URL = 'http://ultimatecowbell.com/songview.php?idsongperm=4247'
page = requests.get(URL)


soup = BeautifulSoup(page.content, "html.parser")

data = soup.find_all('b')

print(data)