# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 14:01:34 2019

@author: Christopher Green
"""

'''
from kafka import KafkaProducer
import time
import json

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
topic = 'UUID'
#this is what we do
#<implement a file reading functionality or any log reader and put it in lines>
for line in lines:
    lst = line.split("Dance Dance Revolution")
try:
    final_list = [lst[x] for x in range(14)]
    producer.send(topic, final_list[0]).get(timeout=10)
except IndexError as e:
    print (e)
    #continue
'''

from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')
bracket = "{"
for _ in range(3):
    print(producer.send('test', b'"worker_id": "worker_id", "key_id": "key_id", "filename": "filename", "filepath": "filepath"'))
    #producer.send('test', "{b'topic2': 'tested', 'key_id': 'key_id'}")
    #print("YUP")

 