import os

base_dir =os.getcwd()
dockercmd = 'docker run --rm -v '
malwarecmd = '\\malware:ro '
cFile = os.path.basename(__file__)
print(type(dockercmd))
print(type(malwarecmd))
print(type(base_dir))
scannerProgram = 'cgreen010/fprot-centos7 '

for file in os.listdir('.'):
    if file is not cFile and 'json' not in file:
        print(dockercmd+base_dir+":"+malwarecmd+scannerProgram+file)
        os.system(dockercmd + base_dir + ":" + malwarecmd + scannerProgram + file)
        f = open(file + ".json", 'w')
        
