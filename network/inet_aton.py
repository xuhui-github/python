#!/usr/bin/python

import socket
from socket import inet_aton,inet_ntoa
import struct

print "local host addr is {}".format(inet_aton('127.0.0.1'))
print inet_ntoa(inet_aton('127.0.0.1'))
pack_addr=socket.inet_pton(socket.AF_INET,'127.0.0.1')
print socket.inet_ntop(socket.AF_INET,pack_addr)
print struct.unpack("=I",socket.inet_aton("127.0.0.1"))
print socket.inet_ntoa(struct.pack('=I',1077545662))
