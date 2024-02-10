from sqlalchemy import select
from sqlalchemyUse import cookies
import sqlite3

connection = sqlite3.connect("./orders.db")
# s = select([cookies])

s = select(cookies)
print(str(s))
rp = connection.execute(str(s))
result = rp.fetchall()
print(result)

s = select(cookies.c.cookie_name, cookies.c.quantity)
rp = connection.execute(str(s))
print(rp)
result = rp.fetchall()
print(result)


s = select(cookies.c.cookie_name, cookies.c.quantity)
s = s.order_by(cookies.c.quantity)
rp = connection.execute(str(s))
print(str(s))
for cookie in rp:
    print("{} - {}".format(cookie[0], cookie[1]))
    # print(cookie[0],cookie[1])

from sqlalchemy import desc

s = select(cookies.c.cookie_name, cookies.c.quantity)
s = s.order_by(desc(cookies.c.quantity))
from sqlalchemy import Connection  # 导入Connection
from sqlalchemy import create_engine
from sqlalchemyUse import engine  # 导入engine

connection1 = Connection(engine)  # 获取connection
print("------engine connection-----")
rp = connection1.execute(s)
for cookie in rp:
    print(cookie.cookie_name, cookie.quantity)

print("------end-------")
print(str(s))
rp = connection.execute(str(s))
for cookie in rp:
    print(cookie)
