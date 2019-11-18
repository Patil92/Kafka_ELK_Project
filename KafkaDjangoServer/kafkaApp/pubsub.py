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
        news = text_data_json['message']
        
        print(" ----PUBSUB---- ",news)
        
        # self.send(text_data=json.dumps({
        #     'message': "Sending "+ news+" data.."
        # }))
        
        from kafka import KafkaConsumer
        
        consumer=KafkaConsumer('TECH',bootstrap_servers=['localhost:9092'],
             auto_offset_reset='earliest',
             enable_auto_commit=True,
             group_id='my-group',
             value_deserializer=lambda x: json.loads(x.decode('utf-8')))
        
        lat=long=0
        
        for mess in consumer:
            print(mess.value)
            
            self.send(text_data=json.dumps({
            'message': mess.value['NEWS']
            }))
            
            
        
        