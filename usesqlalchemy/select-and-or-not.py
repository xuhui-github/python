from sqlalchemy import Connection
from sqlalchemy import and_, or_, not_, select 
from sqlalchemyUse import cookies
from sqlalchemyUse import engine



connection = Connection(engine)

s = select(cookies).where( and_(
    cookies.c.quantity > 23,
    cookies.c.unit_cost < 0.40
    )
                          )

for row in connection.execute(s):
    print(row.cookie_name)

s = select(cookies).where(
        or_(
            cookies.c.quantity.between(10,50),
            cookies.c.cookie_name.contains('chip')
            )
        )

for row in connection.execute(s):
    print(row.cookie_id,row.cookie_name)
