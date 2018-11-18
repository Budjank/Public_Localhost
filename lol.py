import os,sys,time
os.system("clear")
a=raw_input("Port : ")
time.sleep(2)
print "Tunggu Sebentar..."
time.sleep(2)
print "http://localhost:"+a+""

os.system("""
ssh -R 80:localhost:"""+a+""" serveo.net
""")
