from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        
        print("----> Message group --> ",message)
        # Send message to WebSocket
        i=0
        
        '''
        self.send(text_data=json.dumps({
                'message': message
            }))
            
        
        while True:
            
            self.send(text_data=json.dumps({
                'message': str(i)
            }))
            i+=1'''
        
        from kafka import KafkaConsumer
        
        consumer=KafkaConsumer(message,bootstrap_servers=['localhost:9092'],
             auto_offset_reset='earliest',
             enable_auto_commit=True,
             group_id='my-group',
             value_deserializer=lambda x: json.loads(x.decode('utf-8')))
    
        lat=long=0
        
        for mess in consumer:
            print("--------- NEWS API ----------",mess.value['NEWS'])
            self.send(text_data=json.dumps({
                'message': mess.value['NEWS']
            })) 
            
            #yield JsonResponse({"message": mess.value['NEWS']})
            
    
    
    