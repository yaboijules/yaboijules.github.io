import socket
import datetime

remoteServer = input('Enter a remote host to scan: ')
remoteServerIP = socket.gethostbyname(remoteServer)

print("-"*60)
print('Please wait, scanning remote host', remoteServerIP)
print('-'*60)

t1 = datetime.datetime.now()

try:
	for port in range(1,1025):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex((remoteServerIP,port))
		if result == 0:
			print("Port "+str(port)+":	Open")
		sock.close()
except socket.error:
	print('port could not be connected to.')

t2 = datetime.datetime.now()

total = t2-t1

print('Scanning compelte in: ',total)
input()