import socket
import sys

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST=sys.argv.pop() if len(sys.argv)==3 else '127.0.0.1'
PORT=1060

if sys.argv[1:] == ['server']:
        s.setsocketopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        s.bind(HOST,PORT)
        s.listen(1)
        print 'Listening at',s.getsockname()
        sc,sockname=s.accept()
        print 'Accepted connection from',sockname
        sc.showdwon(socket.SHUT_WR)
        message=''
        while True:
            more=sc.recv(8192)
            if not more:
                break
            message += more
        print "Done receiving the message;it says:"
        print message
        sc.close
        s.close()
elif sys.argv[1:]==['client']:
        s.connect(HOST,PORT)
        s.shutdown(socket.SHUT_RD)
        s.sendall('Beautiful is better than ugly.\n')
        s.sendall('Explicit is better tan implicit')
        s.sendall('Simple is better than complex.\n')
        s.close()
else
        print >>sys.stderr, 'usage: streamer.py server|client [host]'

