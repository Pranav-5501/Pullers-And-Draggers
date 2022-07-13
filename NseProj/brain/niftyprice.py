import requests
from bs4 import BeautifulSoup
from threading import Timer

def price_track():

    #stock_symbol = "SBIN"
    #stock_url = 'https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol='+str(stock_symbol)
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
    #response = requests.get(stock_url, headers=headers)
    #soup = BeautifulSoup(response.text, 'html.parser')
    #data_array = soup.find(id='responseDiv').getText().strip().split(":")
    home_url = "https://www.nseindia.com/"
    res = requests.get(home_url,headers=headers)
    soup1 = BeautifulSoup(res.text, 'html.parser')
    Nifty_data = soup1.find(id='tabList_NIFTY50').getText().strip().split("\n")
    N_price = Nifty_data[1]
    nifty_c = Nifty_data[2].split('(')
    nifty_ch = float(nifty_c[1][:-2])
    #Timer(5, N_price).start()
    return N_price,nifty_ch

N_price,nifty_ch = price_track()
Nifty = float(N_price.replace(',',''))