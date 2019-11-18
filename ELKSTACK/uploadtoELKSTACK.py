import sys
import json
from pprint import pprint
from elasticsearch import Elasticsearch
es = Elasticsearch(
    ['https://search-patil92-tqd2kzuwmlgd6brzs3gtrnrjmq.ap-southeast-1.es.amazonaws.com/'],
    port=9200
)

MyFile= open("convertcsv.json",'r').read()
ClearData = MyFile.splitlines(True)
i=0
json_str=""
docs ={}
for line in ClearData:
    line = ''.join(line.split())
    if line != "},":
        json_str = json_str+line
    else:
        docs[i]=json_str+"}"
        json_str=""
        print(docs[i])
        es.index(index='iicweblogs', doc_type='logs', id=i, body=docs[i])
        i=i+1