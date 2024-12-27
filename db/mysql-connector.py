import mysql.connector
import pprint


connect_args = {
    "host": "localhost",
    "port": 3306,
    "user": "xuhui",
    "password": "flower",
    "use_unicode": True,
}

printer = pprint.PrettyPrinter(indent=1)


db = mysql.connector.connect(**connect_args)

result = db.cmd_query(
    """select * 
        from world.city
        where id=130"""
)

print("Result Directionary\n" + "=" * 17)
printer.pprint(result)
db.close()
