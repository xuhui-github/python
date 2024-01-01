import mysql.connector

db = mysql.connector.connect(
        get_warnings=True,
        raise_on_warnings=True,
        option_files="my.ini",
        )

cursor = db.cursor()

db.get_warnings = False
db.raise_on_warnings = False

cursor.execute( "CREATE SCHEMA IF NOT EXISTS py_test_db")

db.get_warnings = True
db.raise_on_warnings = True

result = db.cmd_query("select 1/0")
warnings = db.get_rows()
for warning in warnings:
    print(warningiiiiiii)
db.close()

