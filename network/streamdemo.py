import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print hasattr(s,'read')
f=s.makefile()
print hasattr(f,'read')

