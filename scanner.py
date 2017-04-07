from socket import *
import sys,time
from datetime import datetime
host=''
max_port=5000
min_port=1
def scan_host(host,port,r_code=1):
	try:
		s=socket(AF_INET,SOCK_STREAM)
		code=s.connect_ex((host,port))
		if code==0:
			r_code=code
		s.close()
	except Exception:
		pass
	
	return r_code

try:
	host=input("Target Host IP: ")
except KeyboardInterrupt:
	print("Intruppetted")
	print("Ending program")
	sys.exit(1)

print("Scan started at %s .."%(time.strftime("%H:%M:%S")))
start_time=datetime.now()

for port in range(min_port,max_port):
	try:
		response=scan_host(host,port)
		if response==0:
			print("port: %d : Open"%(port))
	except Exception:
		pass
stop_time=datetime.now()
total_time=stop_time-start_time
print("Scanning Finished at %s..."%(time.strftime("%H:%M:%S")))
print("Scanning duration: %s..."%(total_time))
