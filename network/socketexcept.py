#!/usr/bin/python

import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    s.connect(('noexistent.hostname.foo.bar',80))
except socket.gaierror as e:
    print e.errno
    print e.strerror
    raise
   
