from sqlalchemy import select
from sqlalchemyUse import cookies
from sqlalchemyUse import engine
from sqlalchemy import Connection
from sqlalchemy import func

connection = Connection(engine)

s = select(func.count(cookies.c.cookie_name).label("inventory_count"))
rp = connection.execute(s)
record = rp.first()
# print(record[0])
# print(record.__class__.__name__)
print("result is ", record.inventory_count)
