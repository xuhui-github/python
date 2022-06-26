#!/usr/bin/python

class Service:
    def _query(self,query,type):
        print('done')

    def execute(self,query):
        self._query(query,'EXECUTE')

Service().execute('my queue')

