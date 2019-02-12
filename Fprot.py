# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 11:40:03 2019

@author: Christopher Green
"""


import json
import os
import shutil

#all files ran through put into the safe folder now must run through fprot
#once ran through fprot the json comes here and we move the necessary files 
def runFprot():
    #import file
    with open('fprot-mass.json') as f:
        data = json.load(f)
    
    #delete unneeded data
    for malware in data['fprot']:
    #    print(malware['infected'], malware['result'])
        del malware ['engine'], malware['database'], malware['updated']
    #print(data)
    listA=data
    
    #create directory for infected and uninfected
    Quarantine=[]
    new_listA = []
    
    for item in listA['fprot']:
        if item['infected'] == True:
            Quarantine.append(item['result'])
        else:
            new_listA.append(item['result'])
    
    #location of files and destination folders
    source = 'C:\\Users\\Christopher Green\\Documents\\Projects\\face-recognition\\Decryption-app\\Json'
    dest1 = "C:\\Users\\Christopher Green\\Documents\\Projects\\face-recognition\\Decryption-app\\Json\\Deleted"
    dest2 = "C:\\Users\\Christopher Green\\Documents\\Projects\\face-recognition\\Decryption-app\\Json\\safe"
    dest3 = "C:\\Users\\Christopher Green\\Documents\\Projects\\face-recognition\\Decryption-app\\Json\\shared-drive1"
    
    files = os.listdir(source)
    #loop through list 
    #moves files to disgnated directory based off infected or not
    for s in files:
        if any(s.startswith(p) for p in new_listA):
            shutil.move(s, dest3)
        elif any(s.startswith(p) for p in Quarantine):
            shutil.move(s, dest1)
    
    #convert back into json for elsastic search infected and result    
    with open ('malware_checked.json', 'w') as f:
         json.dump(new_listA, f, indent=2)


























'''


#convert back into json for elsastic search infected and result    
with open ('malware_checked.json', 'w') as f:
     json.dump(data, f, indent=2)

es = elasticsearch.Elasticsearch()

for node in nodes:
    _id = node['index']
    es.index(index='nodes',doc_type='external',id=_id,body=node)
    '''