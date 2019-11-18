from django.shortcuts import render
from django.conf import settings
import json
from django.http import JsonResponse
from django.utils.safestring import mark_safe

import random

# Create your views here.

def index(req):
    
    return render(req,'index.html',{})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
    

def pubsubAPI(req,news):
    
    #news=req.GET['news']
    print("API CALL...",news)
    from kafka import KafkaConsumer
    from kafka import TopicPartition
    import json

    consumer=KafkaConsumer(news,bootstrap_servers=['localhost:9092'],
         auto_offset_reset='earliest',
         enable_auto_commit=True,
         group_id='my-group',
         value_deserializer=lambda x: json.loads(x.decode('utf-8')))

    lat=long=0
  

    '''
    for mess in consumer:
        print("--------- NEWS API ----------",mess.value['NEWS'])
        yield JsonResponse({"message": mess.value['NEWS']})'''
        
        
        
    return JsonResponse({"message": "NONE"})
    
    
def consume(request):
    return render(request, 'home.html',{})
    
def pubsub(request):
    return render(request, 'pubsub.html',{})
    
    
def channels(req):
    
    return render(req,'chat/homechannel.html',{})
    

def iicdashboard(req):
    
    return render(req,'iicdashboard.html',{})
    
def stocks(req):
    return render(req,'liveStocks.html',{})

class Increment:
    def __init__(self):
        self.i=0
        
        
inc=Increment()

def rand(req):
    
    #r=random.randint(0,1000000)
    
    import json
    
    with open('/home/ubuntu/environment/KafkaDjangoServer/kafkaApp/points.json') as f:
        data = json.load(f)
    
    lat=data["points"][inc.i][1]
    long=data["points"][inc.i][0]
    
    inc.i +=1
    
    if inc.i >30:
        inc.i=0
    
    print(inc.i)
    
    '''
    
    from kafka import KafkaConsumer
    import json

    consumer=KafkaConsumer('Patil92',bootstrap_servers=['localhost:9092'],
         auto_offset_reset='earliest',
         enable_auto_commit=True,
         group_id='my-group',
         value_deserializer=lambda x: json.loads(x.decode('utf-8')))

    lat=long=0
    
    for mess in consumer:
        print(mess.value)
    '''
        
    return JsonResponse({"lat":lat,"long":long,"inc":inc.i})
    
    
    #return JsonResponse({"val":r})
    
    
    
    
    
    