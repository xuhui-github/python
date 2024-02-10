#!/usr/bin/env python
from sqlalchemy import delete
from sqlalchemy import select, Connection
from sqlalchemyUse import cookies, engine

connection = Connection(engine)
u = delete(cookies).where(cookies.c.cookie_name == "dark chocolate chip")
result = connection.execute(u)
print("******delete*******")
print(u)
print("******delete*******")
print("result.rowcount= ", result.rowcount)


s = select(cookies).where(cookies.c.cookie_name == "dark chocolate chip")
result = connection.execute(s).fetchall()
print(len(result))
