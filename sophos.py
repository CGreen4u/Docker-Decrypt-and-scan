

import json
import os
import shutil

#all files need to be ran through sophos first
#this is were the json is sent 
#the decrytion folder is the first of the process that sophos pulls from
#import file
def runSophos():
    with open('mass.json') as f:
        data = json.load(f)
    
    #delete unneeded data
    for malware in data['sophos']:
    #    print(malware['infected'], malware['result'])
        del malware ['engine'], malware['database'], malware['updated']
    #print(data)
    listA=data
    
    #create directory for infected and uninfected
    Quarantine=[]
    new_listA = []
    
    for item in listA['sophos']:
        if item['infected'] == True:
            Quarantine.append(item['result'])
        else:
            new_listA.append(item['result'])
    
    #location of files and destination folders
    source = 'C:\\Users\\Christopher Green\\Documents\\Projects\\face-recognition\\Decryption-app\\Json'
    dest1 = "C:\\Users\\Christopher Green\\Documents\\Projects\\face-recognition\\Decryption-app\\Json\\Deleted"
    dest2 = "C:\\Users\\Christopher Green\\Documents\\Projects\\face-recognition\\Decryption-app\\Json"
    
    files = os.listdir(source)
    #loop through list 
    #moves files to disgnated directory based off infected or not
    for s in files:
        if any(s.startswith(p) for p in new_listA):
            shutil.move(s, dest2)
        elif any(s.startswith(p) for p in Quarantine):
            shutil.move(s, dest1)
    
    #convert back into json for elsastic search infected and result    
    with open ('malware_checked.json', 'w') as f:
         json.dump(new_listA, f, indent=2)





