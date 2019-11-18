from channels.generic.websocket import WebsocketConsumer
import json
import time

class ChatConsumer(WebsocketConsumer):
    
    def connect(self):
        self.accept()
        
        print("######################################  Client Connected....!!!!")
        

    def disconnect(self, close_code):
        pass
    
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        company = text_data_json['message']
        
        print("------ ",company)
        
        self.send(text_data=json.dumps({
            'message': "Sending "+ company+" data.."
        }))
        
        i=0
        
        from alpha_vantage.timeseries import TimeSeries
        import matplotlib.pyplot as plt
        
        API_KEY='PL1OM52PVGUXSR4C'
        ts = TimeSeries(key=API_KEY,output_format='pandas')
        data, meta_data = ts.get_intraday(symbol=company,interval='60min', outputsize='full')
        
        
        data=data['4. close']
        data.to_csv(company+".csv",index = None,header=True)
        
        import pandas as pd
    
        data=pd.read_csv(company+'.csv',delimiter = ',')
        
        i=0
        while True:
            
            if i<len(data):
                
                self.send(text_data=json.dumps(
                {
                    'message': data['4. close'][i]
                }))
                
                i+=1
            else:
                
                data, meta_data = ts.get_intraday(symbol=company,interval='1min', outputsize='full')
                data=data['4. close']
                
                self.send(text_data=json.dumps(
                {
                    'message': data['4. close'][len(data)-1]
                }))
                
            time.sleep(1)
        