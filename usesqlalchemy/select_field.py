from sqlalchemy import Connection
from sqlalchemyUse import engine
from sqlalchemyUse import cookies
from sqlalchemy import select, cast, Numeric

connection = Connection(engine)
s = select(cookies.c.cookie_name, "SKU" + cookies.c.cookie_sku)
print(s)
for row in connection.execute(s):
    print(row)

s = select(
    cookies.c.cookie_name,
    cast((cookies.c.quantity * cookies.c.unit_cost), Numeric(12, 2)).label("inv_cost"),
)
print(s)
for row in connection.execute(s):
    print("{} - {}".format(row.cookie_name, row.inv_cost))
