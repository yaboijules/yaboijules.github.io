import socket

name = 'google.com'

try:
	host = socket.gethostbyname(name)
	print(host)
except socket.gaierror:
	print("cannot resolve hostname: ", name, err)