# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 14:45:26 2019

@author: Christopher Green
"""

# make sure ES is up and running
import requests
res = requests.get('http://localhost:9200')
print(res.content)

#bring in necessary packages
from elasticsearch import Elasticsearch

# by default we don't sniff, ever
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# you can specify to sniff on startup to inspect the cluster and load
# balance across all nodes
es = Elasticsearch(["seed1", "seed2"], sniff_on_start=True)

# you can also sniff periodically and/or after failure:
es = Elasticsearch(["seed1", "seed2"],
          sniff_on_start=True,
          sniff_on_connection_fail=True,
          sniffer_timeout=60)




'''
import requests
data = open('new_malware.json').read()
url = "http://localhost:9200/"
requests.post(url, data=data)
'''
'''
from elasticsearch import Elasticsearch, helpers
import sys, json

es = Elasticsearch()

def load_json(directory):
    " Use a generator, no need to load all in memory"
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            with open(filename,'r') as open_file:
                yield json.load(open_file)

helpers.bulk(es, load_json(sys.argv[1]), index='my-index', doc_type='my-type')
'''