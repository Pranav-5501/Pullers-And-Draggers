import requests
from bs4 import BeautifulSoup
from threading import Timer


home_url = "https://www.nseindia.com/"
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
res = requests.get(home_url,headers=headers)
soup1 = BeautifulSoup(res.text, 'html.parser')
Nifty_data = soup1.find(id='tabList_NIFTY50').getText().strip().split("\n")
N_price = Nifty_data[1]
Nifty = float(N_price.replace(',',''))

#HUL and M&M removed because of issues
stocks_info = {'HDFCBANK':8.38,'RELIANCE':12.51,'INFY':7.58,'HDFC':5.57,'ICICIBANK':7.21,
                'TCS':4.8,'KOTAKBANK':3.73,'ITC':3.26,'AXISBANK':2.49,
                'LT':2.75,'SBIN':2.47,'BAJFINANCE':2.23,'BHARTIARTL':2.28,'ASIANPAINT':1.78,
                'HCLTECH':1.52,'MARUTI':1.46,'ULTRACEMCO':0.97,'SUNPHARMA':1.28,
                'TITAN':1.27,'TECHM':1.01,'WIPRO':0.97,'NESTLEIND':0.87,'TATASTEEL':1.17,
                'BAJAJFINSV':1.08,'HDFCLIFE':0.77,'POWERGRID':1.1,'GRASIM':0.74,'DRREDDY':0.73,
                'INDUSINDBK':0.83,'TATAMOTORS':1.1,'ADANIPORTS':0.73,'NTPC':1.02,'BAJAJ-AUTO':0.69,
                'HINDALCO':0.85,'DIVISLAB':0.63,'JSWSTEEL':0.73,'BRITANNIA':0.59,'CIPLA':0.71,
                'BPCL':0.43,'SHREECEM':0.41,'HEROMOTOCO':0.50,'ONGC':0.76,'EICHERMOT':0.53,
                'UPL':0.59,'SBILIFE':0.71,'COALINDIA':0.56,'TATACONSUM':0.63,'APOLLOHOSP':0.37}
stocks = list(stocks_info.keys())

stock_chg = []
stock_val = []
stock_pt = []
NIFTY = Nifty

for stock in stocks:

    stock_url = 'https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol='+str(stock)
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
    response = requests.get(stock_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    data_array = soup.find(id='responseDiv').getText().strip().split(":")
    #to  find changes in percentages

    lp = 0
    for item in data_array:
        if 'lastPrice' in item:
            lp = data_array.index(item) + 1
    lst_prc = data_array[lp].split('"')
    val = lst_prc[1]
    stock_val.append(val)

    n = 0
    for item in data_array:
        if 'pChange' in item:
            n = data_array.index(item) + 1
    sp = (data_array[n].split(','))
    sp1 = sp[0]
    change = float(sp1[1:-1])
    stock_chg.append(change)

    # to find last price
    

    stocks_info = {'HDFCBANK':10.24,'RELIANCE':10.19,'INFY':7.98,'HDFC':7.08,'ICICIBANK':6.34,
                'TCS':5.18,'KOTAKBANK':4.05,'ITC':3.01,'AXISBANK':2.76,
                'LT':2.70,'SBIN':2.20,'BAJFINANCE':2.15,'BHARTIARTL':1.97,'ASIANPAINT':1.80,
                'HCLTECH':1.68,'MARUTI':1.44,'ULTRACEMCO':1.22,'SUNPHARMA':1.02,
                'TITAN':1.02,'TECHM':0.97,'WIPRO':0.96,'NESTLEIND':0.96,'TATASTEEL':0.96,
                'BAJAJFINSV':0.92,'HDFCLIFE':0.91,'POWERGRID':0.87,'GRASIM':0.87,'DRREDDY':0.86,
                'INDUSINDBK':0.85,'TATAMOTORS':0.85,'ADANIPORTS':0.81,'NTPC':0.80,'BAJAJ-AUTO':0.75,
                'HINDALCO':0.75,'DIVISLAB':0.73,'JSWSTEEL':0.71,'BRITANNIA':0.67,'CIPLA':0.65,
                'BPCL':0.63,'SHREECEM':0.62,'HEROMOTOCO':0.60,'ONGC':0.59,'EICHERMOT':0.57,
                'UPL':0.56,'SBILIFE':0.54,'COALINDIA':0.43,'TATACONSUM':0.42,'APOLLOHOSP':0.37}


    for key, value in stocks_info.items():
            if key == stock:
                Weightage = value

    w_move = (change * Weightage) / 10000
    index = NIFTY * w_move;
    stock_points = ("%.2f" % index)
    stock_pt.append(stock_points)

"""print(stocks)
print(stock_val)
print(stock_chg)
print(stock_pt)
    """



#INFY_val,INFY_change,INFY_points = price(NIFTY)