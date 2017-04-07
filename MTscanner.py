'''
This is a Multithreaded TCP port scanner. On my machine it can scan all ports in 30 seconds.
'''
from socket import *
import sys,time
from datetime import datetime
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool 
#thredcount=
pool = ThreadPool(32768)
host=''
max_port=65536
min_port=1
ports=[x for x in range(min_port,max_port)]
def scan_host(port):
	try:
		r_code=1
		s=socket(AF_INET,SOCK_STREAM)
		code=s.connect_ex((host,port))
		if code==0:
			return port
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

'''def scan():
	try:
		response=scan_host(host,port)
		if response==0:
			return port
	except Exception:
		pass'''
		
open_ports=pool.map(scan_host,ports)
reduced=[port for port in open_ports if port>1]
pool.close()
pool.join()
stop_time=datetime.now()
total_time=stop_time-start_time
print("Open Ports are")
print(reduced)
print("Scanning Finished at %s..."%(time.strftime("%H:%M:%S")))
print("Scanning duration: %s..."%(total_time))
