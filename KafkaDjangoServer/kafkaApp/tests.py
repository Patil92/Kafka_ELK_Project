from django.test import TestCase

# Create your tests here.

import json
import time 


def readjson():
    with open('points.json') as f:
        data = json.load(f)
    
    
    print(len(data["points"]))
    print(data["points"][0])

def getcurrentStock():
    from alpha_vantage.timeseries import TimeSeries
    import matplotlib.pyplot as plt
    
    API_KEY='PL1OM52PVGUXSR4C'
    ts = TimeSeries(key=API_KEY,output_format='pandas')
    data, meta_data = ts.get_intraday(symbol='AMZN',interval='60min', outputsize='full')
    
    # data.plot()
    # plt.title('BBbands indicator for  MSFT stock (60 min)')
    # plt.show()
    # plt.savefig('stock.jpg')
    
    data=data['4. close']
    
    data.to_csv("./stocks_csv/MSFT.csv",index = None,header=True)
    
    print(data.head(3))
    print("\n\n")
    print(data.tail(3))
    print("\n\n")
    print(len(data))
    
    
def readStocksCSV():
    
    import pandas as pd
    
    data=pd.read_csv('./stocks_csv/MSFT.csv',delimiter = ',')
    #print(data.head(3))
    # data=pd.DataFrame([da], columns = ["Time", "Value"])
    
    i=0
    
    # while i<len(data):
    #     print(data.loc[i])
    #     i+=1
    #     time.sleep(3)
    print(data['4. close'][5]) 
    print(len(data))
    data=data['4. close'][len(data)-1]
    
    
    print(data)
    #print(len(data),data.index,data.head(3))
    
#getcurrentStock()

readStocksCSV()

    