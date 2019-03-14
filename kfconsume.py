# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 13:52:36 2019

@author: Christopher Green
"""
'''
from kafka import KafkaConsumer
topic = 'test'
consumer = KafkaConsumer(topic, bootstrap_servers=['localhost:9092'])
print(type(consumer))

for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    # print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
    #                                       message.offset, message.key,
    #                                       message.value))
    print message
    
#Source
#https://stackoverflow.com/questions/35689238/kafka-python-producer-is-not-able-to-connect
'''


from kafka import KafkaConsumer

def bytesToDictionary(b_array):
     d = dict(toks.split(":") for toks in b_array.decode("utf-8").split(",") if toks)
     #print("Convert")
     return d
consumer = KafkaConsumer('test')
print(type(consumer))
cargo = []
for msg in consumer:
    print(msg)
    d = bytesToDictionary(msg.value)
    s = msg.value.decode("utf-8")
    #if msg.value == key_id:
         #cargo.append(key_id)
         #print (msg)
    if 'key_id' in s:
         cargo.append(d['key_id'])
    print(cargo)
    print(d)
