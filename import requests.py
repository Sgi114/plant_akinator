import requests
from bs4 import BeautifulSoup



URL = requests.get('http://www.io-net.com/violet/violet1/sumiresaisin.htm')
URL.encoding = URL.apparent_encoding  # 呪文
soup = BeautifulSoup(URL.text,'html.parser')

viola = {}

table = soup.find('table')
tbody = table.find('tbody')
trs = tbody.find_all('tr')  # trタグを探す


for tr in trs: 
    for th in tr.find_all('th'):  # trタグからthタグを探す
        if not th.get('rowspan'):
            viola[th.text] = 'x' 
    for td in tr.find_all('td'):  # trタグからtdタグを探す
        viola[th.text] = td.text
    
print(viola)

# viola[r] = s
# print(viola)
