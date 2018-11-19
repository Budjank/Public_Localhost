import os,sys,time
os.system("clear")
a=raw_input("Port : ")
b=raw_input("Subdo : ")
time.sleep(2)
print "Tunggu Sebentar..."
time.sleep(2)
print "http://localhost:"+a+""

os.system("""
ssh -R """+b+""".serveo.net:80:localhost:"""+a+""" serveo.net
""")
