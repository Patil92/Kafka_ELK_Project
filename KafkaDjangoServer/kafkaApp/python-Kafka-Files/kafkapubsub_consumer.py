from kafka import KafkaConsumer
import json


consumer=KafkaConsumer('TECH',bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: json.loads(x.decode('utf-8')))

for mess in consumer:
    print(mess.value['NEWS'])