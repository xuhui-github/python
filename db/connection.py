#!/usr/bin/python
class DBTest:
    
    def connection(self):
        """
        Creates a database connection and returns the cursor. All login 
        information is hardwired.
        HOST=localhost
        USER=xuhui
        DATABASE=sakila
        """
        try:
            con = MySQLdb.connect(host = 'localhost',
                    user = 'xuhui',
                    passwd = 'flower',
                    db = 'sakila')
            cur = con.cursor()
            return cur
        except MySQLdb.Warning:
            pass
        except MySQLdb.Error:
            print("There was a problem in connectiong to the database.\nPlease ensure that the 'sakila' database exists on the local host system")
            return None
    
    def query(self):

