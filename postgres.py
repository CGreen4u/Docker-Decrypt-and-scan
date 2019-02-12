# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 11:18:36 2019

@author: Christopher Green
"""
#!/usr/bin/python

import psycopg2

conn = psycopg2.connect(database="testdb", user = "postgres", password = "pass123", host = "127.0.0.1", port = "5432")

print "Opened database successfully"

cur = conn.cursor()

cur.execute("SELECT UUid, name, Passphrase, secret key, private key  from COMPANY")
rows = cur.fetchall()
for row in rows:
   print "ID = ", row[0]
   print "NAME = ", row[1]
   print "PASSPHRASE = ", row[2]
   print "SECRET KEY = ", row[3], 
   print "PRIVATE KEY = ",row [4], "\n"
print "Operation done successfully";
conn.close()

