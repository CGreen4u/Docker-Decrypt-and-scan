# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 14:45:26 2019

@author: Christopher Green
"""
'''
# make sure ES is up and running
import datetime
import requests
res = requests.get('http://localhost:9200')
print(res.content)

#sophos_virus_dis = ["run", "fast", "dont", "die"]
#clean_fx = ["we", "the", "people"]

from elasticsearch import Elasticsearch

INDEX = 'malware'
#need this for congifuration
LOG_HOST = 'myhost:myport'
logserver = Elasticsearch([{'host':'localhost','port':9200}])

script = "ctx._source.attribute = new_value"

update_body = {
    "query": {
        "constant_score" : {
            "filter" : {
                 "bool" : {
                    "must" : [
                        { "term" : { "tags" : "clamav" } }, 
                        { "term" : { "location" : "Quarantine" } },
                        { "terms" : { "Clam_AV" : clamscan_virus_dis } },
                    ]
                }
            }
        }
    },
                  "query": {
        "constant_score" : {
            "filter" : {
                 "bool" : {
                    "must" : [
                        { "term" : { "tags" : "sophos" } }, 
                        { "term" : { "location" : "Quarantine" } },
                        { "terms" : { "Sophos" :  sophos_virus_dis } },
                    ]
                }
            }
        }
    },
                  "query": {
        "constant_score" : {
            "filter" : {
                 "bool" : {
                    "must" : [
                        { "term" : { "tags" : "clean_files" } }, 
                        { "term" : { "location" : "shared_folder1" } }, 
                        { "terms" : { "Clean_files" :  clean_fx } },
                    ]
                }
            }
        }
    }
}

update_response = logserver.index(index=INDEX, doc_type = body=update_body)

'''
#Define the schema
#-------------------------
#This should match the schema for your ES index exactly including capitalization.
#-------------------------
lead_UUID = ["1334958ford", "20234lotus", "speed12310", "03852maserati","wish09876"]
lead_type = ["F54", "F46", "F234"]

from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Search, UpdateByQuery, Text, Date, Integer , Document, Index, DocType


class ES_Lead(Document):
    lead_UUID = Text()
    lead_type = Text()
    lead_creation_date = Date()
    lead_creation_user_UUID = Text()

    class Index:
        # Name of the ES Index
        name = "leads10"

class ES_LookUp_Writer:
    def __init__(self):
        self.create_lookup()

     #Build the connection
     #Make the connection to Elastic Search
    def create_connection(self):
               self.conn = connections.create_connection(
                                           hosts=['localhost'])

     #Logic: IF the lookUp name does NOT exist create the lookup and add the values provided
     #       ELSE pass the record to the update lookup function.
    def create_lookup(self):
        self.create_connection()
        result = ES_Lead(lead_UUID="1239f03" , lead_type="72390go",lead_creation_date="1999-12-23T15:45:00+08:00", lead_creation_user_UUID="John50").save()
       
ES_LookUp_Writer()


'''

#class ES:
#    variable = "elasticfunction"

#    def elasticsearch(self):


sophos = ["fist", "cat", "car"]
clam = ["run", "fast", "dont", "die"]
clean = ["we", "the", "people"]

from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Search, UpdateByQuery, Text, Date, Integer , Document, Index, DocType

connections.create_connection(hosts=['localhost'])

class ES_file(Document):
    sophos = Text()
    clam = Text()
    clean = Text()
    
    class Index:
        name = "malware"
    class Meta:
        doc_type = 'json'
    
class ES_file_writer:
    def __init__(self, task, **kwargs):
        self.sophos = kwargs["sophos"]
        self.clam = kwargs["clam"]
        self.clean = kwargs["clean"]
        
        if task == "update_file":
            self.update_file()
        elif task == "upload_file":
            a = 1
        
    def save(self, **kwargs):
        self.created_at = datetime.now()
        return super(ES_file, self).save(**kwargs)


ES_file = ES_file()    
ES_file.save()


result = doc.update(MalwareFoundIn=self.sophos, CleanFileCategory=self.clean)
'''
    
#search for alternative method outside of UpdatebyQuery
"""

client = Elasticsearch([{'host':'localhost','port':9200}])
ubq = Update(using=client, index="clamscan_virus_dir", "sophos_virus_dir" , "clean_files") \
      .query("match", title="Malware_chec")   \
      .exclude("match", description="malware", "scanned_by_sophos" , "scanned_by_clamav" ) \
      .script(source="ctx._source.like", lang="painless")
#ubr = search(using=client, index="sophos_virus_dir") \
#     .query("match", title="python")   \
#      .exclude("match", description="malware") \
#      .script(source="ctx._source.likes", lang="painless")
#ubs = UpdateByQuery(using=client, index="clean_files") \
#      .query("match", title="python")   \
#      .exclude("match", description="malware_free") \
#      .script(source="ctx._source.likes", lang="painless")


response = ubq.execute() 
#, ubr.execute(), ubs.execute()
"""