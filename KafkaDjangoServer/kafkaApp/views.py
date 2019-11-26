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

class Distance:
    def __init__(self,l1,l2):
        self.lat=l1
        self.long=l2
        
dist=Distance(12.313237,76.613519)

from math import cos, asin, sqrt

def distance(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295
    a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a))
    
def sendEmail(st):
    
    try:
        import smtplib 
        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.starttls() 
        s.login("Abhishekspatil92@gmail.com", open("/home/ubuntu/environment/KafkaDjangoServer/kafkaApp/password.txt", "r").read()) 
        s.sendmail("Abhishekspatil92@gmail.com", "spbharath96@yahoo.com", st)
        s.quit()
        
        print("Sent Email")
    except Exception:
        print("Some Error Happened Sending Email.. Try again or Contact Patil92")
    
    
class SendEmailCheck():
    def __init__(self):
        self.FlagSendEmail=True

flagemail=SendEmailCheck()

def rand(req):
    
    #r=random.randint(0,1000000)
    from firebase import firebase
    firebase = firebase.FirebaseApplication('https://saving-9f42a.firebaseio.com/', None)
    result = firebase.get('/Apart/Users/user1/location', None)
    #print(result['latitude'],result['longitude'])
    inc.i +=1
    
    di=distance(result['latitude'],result['longitude'],dist.lat,dist.long)
    
    if di<10:
        if flagemail.FlagSendEmail:
            sendEmail("Welcomes to Patil's World..!! /n/n Vehicle is Nearer to Manasagangotri Police Station")
            flagemail.FlagSendEmail= False
        else:
            print("Email Already Sent waiting For Ack..!!")
        
    print("Distance In Km : ",di)
    
    return JsonResponse({"lat":result['latitude'],"long":result['longitude'],"inc":inc.i})
    #{'1': 'John Doe', '2': 'Jane Doe'}
    
    '''
    import json
    
    with open('/home/ubuntu/environment/KafkaDjangoServer/kafkaApp/points.json') as f:
        data = json.load(f)
    
    lat=data["points"][inc.i][1]
    long=data["points"][inc.i][0]
    
    inc.i +=1
    
    if inc.i >30:
        inc.i=0
    
    print(inc.i)
    
    
    
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
    
    
    return JsonResponse({"lat":lat,"long":long,"inc":inc.i})
    '''
    
    #return JsonResponse({"val":r})
    
    
    
    
    
    