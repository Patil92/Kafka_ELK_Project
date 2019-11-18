from kafka import KafkaProducer
import json
import time

producer=KafkaProducer(bootstrap_servers="localhost:9092",value_serializer=lambda v:json.dumps(v).encode('utf-8'))

i=0

import json
    
with open('/home/ubuntu/environment/KafkaDjangoServer/kafkaApp/points.json') as f:
    jsondata = json.load(f)

while True:
    data={
        "Name":"Patil",
        "latitude": jsondata["points"][i][1],
        "longitude": jsondata["points"][i][0],
        "Count": i
    }
    
    if i==30:
        break
    
    print(data)

    producer.send("Patil92",data)
    i+=1
    time.sleep(2)


# while True:
#     str=input("Enter Message : ")
    
#     if str=="Stop":
#         break

#     producer.send("Patil92",str.encode())
    
    