import requests
from bs4 import BeautifulSoup
from threading import Timer
from brain import niftyprice


def price(Nifty):

    stock_symbol = "HDFC"
    stock_url = 'https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol='+str(stock_symbol)
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
    response = requests.get(stock_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    data_array = soup.find(id='responseDiv').getText().strip().split(":")
    #to  find changes in percentages
    for item in data_array:
        if 'pChange' in item:
            index = data_array.index(item) + 1
    sp = (data_array[index].split(','))
    sp1 = sp[0]
    HDFC_change = float(sp1[1:-1])

    # to find last price
    lp = 0
    for item in data_array:
        if 'lastPrice' in item:
            lp = data_array.index(item) + 1
    lst_prc = data_array[lp].split('"')
    HDFC_val = lst_prc[1]

    stocks_info = {'HDFCBANK':10.24,'RELIANCE':10.19,'INFY':7.98,'HDFC':7.08,'ICICIBANK':6.34,
                'TCS':5.18,'KOTAKBANK':4.05,'HUL':3.42,'ITC':3.01,'AXISBANK':2.76,
                'LT':2.70,'SBIN':2.20,'BAJFINANCE':2.15,'BHARTIARTL':1.97,'ASIANPAINT':1.80,
                'HCLTECH':1.68,'MARUTI':1.44,'ULTRACEMCO':1.22,'M&M':1.20,'SUNPHARMA':1.02,
                'TITAN':1.02,'TECHM':0.97,'WIPRO':0.96,'NESTLEIND':0.96,'TATASTEEL':0.96,
                'BAJAJFINSV':0.92,'HDFCLIFE':0.91,'POWERGRID':0.87,'GRASIM':0.87,'DRREDDY':0.86,
                'INDUSINDBK':0.85,'TATAMOTORS':0.85,'ADANIPORTS':0.81,'NTPC':0.80,'BAJAJ-AUTO':0.75,
                'HINDALCO':0.75,'DIVISLAB':0.73,'JSWSTEEL':0.71,'BRITANNIA':0.67,'CIPLA':0.65,
                'BPLC':0.63,'SHREECEM':0.62,'HEROMOTOCO':0.60,'ONGC':0.59,'EICHERMOT':0.57,
                'UPL':0.56,'SBILIFE':0.54,'COALINDIA':0.43,'TATACONSUM':0.42,'IOC':0.37}


    for key, value in stocks_info.items():
            if key == stock_symbol:
                Weightage = value

    w_move = (HDFC_change * Weightage) / 10000
    index = Nifty * w_move;
    HDFC_points = ("%.2f" % index)
    return(HDFC_val,HDFC_change,HDFC_points)


NIFTY = niftyprice.Nifty
HDFC_val,HDFC_change,HDFC_points = price(NIFTY)