from sqlalchemy import Connection
from sqlalchemy import select
from sqlalchemyUse import engine
from sqlalchemyUse import cookies

connection = Connection(engine)
s = select(cookies).where(cookies.c.cookie_name.like("%chocolate%"))
rp = connection.execute(s)
for record in rp.fetchall():
    print(record.cookie_name)
