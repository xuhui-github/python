#!/usr/bin/python

class Connection:
    _connections=[]

    def connect(self,usr):
        self._connections.append(usr)

    def connected_people(self):
        return ','.join(self._connections)

class Database:
    def __init__(self):
        pass
class User:
    pass


con=Connection()
con.connect('con1')
con.connect('con2')
print con.connected_people()

