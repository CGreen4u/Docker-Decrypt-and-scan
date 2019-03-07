# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 12:57:19 2019

@author: Christopher Green
"""
import psycopg2
import sys
import os
import fs
from fs import open_fs
import gnupg
import config
import subprocess
import os
import shutil
import tarfile
from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Search, UpdateByQuery, Text, Date, Integer , Document, Index, DocType




class postgres_UUID:
    def post_connect():
            conn = psycopg2.connect(database="dvdrental", user = "postgres", password = "pass123", host = "127.0.0.1", port = "5432")

    def querying_data():
        cur = conn.cursor()
        #first_name and actor_id are stand in components and need to be changd to UUID and public-key
        cur.execute("SELECT DISTINCT first_name, actor_id FROM actor t WHERE  actor_id = '120'")
        rows = cur.fetchall()
        public_keyring.clear()
        location_encryped_file.clear()
        
        for row in rows:
           public_keyring=(row[0])
           location_encryped_file = (row[1])
        #   print "passphrase = ", row[5]
        #   print "SECRET-KEY = ", row[3], 
        #   print "PRIVATE-KEY = ",row [4], "\n"
        print ("Operation done successfully");
        conn.close()

postgres_UUID()

 #open in /Decrytion run enviorment venv/bin/activate 

#source folder
#postgres for uuid location
#may need to talk to kafka to know the location - no 
#home is the encrypted folder shared 0
#gpg = gnupg.GPG(gnupghome='/home/cgreen/Decryption/Encrypted')

class Decryption:
    def decrpt_location_key():
        public_keyring= "forest"
        
        gpg = gnupg.GPG(gnupghome=location_encryped_file,
                                        gpgbinary='gpgbinary',
                                        keyring= public_keyring)
        
        #secret key needs to be included here
        home_fs = open_fs(".")
        
        #create directory
        files_dir = []
        files_dir_clean = []
        #create seperate path for decryped files to be seperate from encryped files
        if os.path.exists("decrypted/"):
            print("Decrypted directory already exists")
        else:
            home_fs.makedir(u"decrypted/")
            print("Created decrypted directory")
        
    def clean_list_decrypted():    
        #add files to list (list the uuid for the folder to pick) name of file from kafka
        files = [f for f in os.listdir(".") if os.path.isfile(f)]
        for f in files:
            files_dir.append(f)
        
        #remove the .gpu from the file 
        for x in files_dir:
            length = len(x)
            endLoc = length - 4
            clean_file = x[0:endLoc]
            files_dir_clean.append(clean_file)
        
    def final_decryption():
        #decryped files.  Be sure the passphrase is properly named. 
        for x in files_dir:
             	with open('encryped location', 'rb') as f:
            	  		status = gpg.decrypt_file(f, passphrase='greenzone1', output=files_dir_clean[files_dir.index(x)])
                          #greenzone1
        print( 'ok: ', status.ok)
        print( 'status: ', status.status)
        print( 'stderr: ', status.stderr)
        os.rename(files_dir_clean[files_dir.index(x)], "decrypted/" + files_dir_clean[files_dir.index(x)])
               
        print("Decryption Complete")
        
Decryption()

#configure location
#def run.malwarecheck()
#clamscan will move it into another folder for us but sophos will not
class malware_scanner:
    def malware_location():
        clamscan_virus_dir = []
        sophos_virus_dir = []
        clean_files = []
        changes = []
        
        #create seperate path for files to be seperated
        if os.path.exists("//home//cgreen//Decryption//Json//virus"):
            pass
        else:
            os.mkdir(u"//home//cgreen//Decryption//Json//virus")
        if os.path.exists("//home//cgreen//Decryption//Json//shared-drive1"):
            pass
        else:
            os.mkdir(u"//home//cgreen//Decryption//Json//shared-drive1")    
        #location of files and desingated folders
        source = '//home//cgreen//Decryption//Json'
        dest1 = "//home//cgreen//Decryption//Json//shared-drive1"
        dest3 = "//home//cgreen//Decryption//Json//virus"
        
        files = os.listdir(source)
    def malware_bash():
        #Run command on command line to start the first malware scanner
        bashCommand = "clamscan -r --move=//home//cgreen//Decryption//Json//virus //home//cgreen//Decryption//decrypted//"
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        for root, dirs, files in os.walk("//home//cgreen//Decryption//Json//virus"):
              for file in files:
                clamscan_virus_dir.append(file)
        
        #bashCommand2 = "sweep /home/cgreen/decrypted --quarantine=//home//cgreen//Decryption//Json//virus" 
        #process = subprocess.Popen(bashCommand2.split(), stdout=subprocess.PIPE)
        #output, error = process.communicate()
        #for root, dirs, files in os.walk("/virus"):
        #    for file in files:       
        #        changes.append(file)
        #sophos_virus_dir.append(list(set(changes) - set(clamscan_virus_dir)))
        
        #the infected files are alread in quarantine we only need to move the original files 
        base_path = "//home//cgreen//Decryption//decrypted//"
        for root, dirs, files in os.walk("//home//cgreen//Decryption//decrypted//"):
            for file in files:#, root, dirs:
                tar = tarfile.open("//home//cgreen//Decryption//Json//shared-drive1//" + "sample.tar.gz", "w:gz")
                tar.add(base_path + file)
                tar.close()
        clean_files = os.listdir("//home//cgreen//Decryption//Json//shared-drive1//")
                #clean_files[shutil.move(base_path + file, dest1)]
malware_scanner()        


class Elasticseach_for_malware:
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
