from kafka import KafkaProducer
import json
import time

producer=KafkaProducer(bootstrap_servers="localhost:9092",value_serializer=lambda v:json.dumps(v).encode('utf-8'))

i=0
while True:
    
    prod=input("Enter Producer...")
    news=input("Enter TECH Updates : ")
    #k=str(i)+str(i)+str(i)
    data={
        "Name":"Patil92",
        "NEWS":news,
        "Count": i
    }
    
    print(data)

    producer.send("TECH",data)
    i+=1
    time.sleep(5)


# while True:
#     str=input("Enter Message : ")
    
#     if str=="Stop":
#         break

#     producer.send("Patil92",str.encode())
    
    