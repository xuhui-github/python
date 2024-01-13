from sqlalchemyUse import engine
from sqlalchemy import Connection
from sqlalchemyUse import cookies
from sqlalchemy import select

connection = Connection(engine)

s=select(cookies).where(cookies.c.cookie_name == 'chocolate chip')
rp = connection.execute(s)
record =rp.first()
print(record)
