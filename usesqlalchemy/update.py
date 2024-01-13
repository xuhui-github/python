from sqlalchemy import update
from sqlalchemy import select
from sqlalchemy import Connection
from sqlalchemyUse import cookies
from sqlalchemyUse import engine
from sqlalchemyUse import customer
connection = Connection(engine)
u = update(cookies).where(cookies.c.cookie_name == 'chocolate chip')
u = u.values(quantity=(cookies.c.quantity + 120))
print("u= **********************",u)
result = connection.execute(u)
print(result.rowcount)

s = select(cookies).where(cookies.c.cookie_name == "chocolate chip")
result = connection.execute(s).first()
for field in result:
    print("{:>50}".format(field))
