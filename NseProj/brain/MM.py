import requests
from bs4 import BeautifulSoup

home_url = "https://www.nseindia.com/"
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
res = requests.get(home_url,headers=headers)
soup1 = BeautifulSoup(res.text, 'html.parser')
Nifty_data = soup1.find(id='tabList_NIFTY50').getText().strip().split("\n")
N_price = Nifty_data[1]
Nifty = float(N_price.replace(',',''))

HUL_weightage = 1.52
stock_symbol = "HU"
stock_url = 'https://www.moneycontrol.com/india/stockpricequote/personal-care/hindustanunilever/MM'
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
response = requests.get(stock_url, headers=headers)
#print(response)
soup = BeautifulSoup(response.text, 'html.parser')
data_array = soup.find(id='nsecp').getText().strip().split(":")
data_chg = soup.find(id='nsechange').getText().strip().split(":")
MM_price = float(data_array[0].replace(',',''))
y = data_chg[0].split('(')
z = (y[1].split('%'))
MM_change = float(z[0])


#calculation
w_move = (MM_change * HUL_weightage) / 10000
index = Nifty * w_move;
stock_points = ("%.2f" % index)
