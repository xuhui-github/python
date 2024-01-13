import MySQLdb
con = MySQLdb.connect('localhost','xuhui','flower','employees')
cur=con.cursor();
count = cur.execute('select * from employees limit 10')
print("found %d records" % count)
for record in cur.fetchall():
    print(record)


last_name = 'Facello'
print("...")
cur = con.cursor()
command = cur.execute(
        """
        select * from employees where last_name = '%s'
        """
        % last_name)
results = cur.fetchall()
for record in results:
    print(record[0],record[2],record[3])

print("hello")
statement = """show tables"""
cur.execute(statement)
results = cur.fetchall()
for result in results:
    print(result[0])
cur.close()
con.close()

                                          
