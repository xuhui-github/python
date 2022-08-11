from datetime import datetime
from sqlalchemy import DateTime
from sqlalchemy import PrimaryKeyConstraint,UniqueConstraint,CheckConstraint
from sqlalchemy import ForeignKey
from sqlalchemy import Table,Column,Integer,Numeric,String,ForeignKey
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Boolean
from sqlalchemy import select


metadata=MetaData()


cookies=Table('cookies',metadata,
        Column('cookie_id',Integer(),primary_key=True),
        Column('cookie_name',String(50),index=True),
        Column('cookie_recipe_url',String(255)),
        Column('cookie_sku',String(55)),
        Column('quantity',Integer()),
        Column('unit_cost',Numeric(12,2))
        )

users=Table('users',metadata,
        Column('user_id',Integer(),primary_key=True),
        Column('username',String(15),nullable=False,unique=True),
        Column('email_address',String(255),nullable=False),
        Column('phone',String(20),nullable=False),
        Column('password',String(25),nullable=False),
        Column('created_on',DateTime(),default=datetime.now),
        Column('updated_on',DateTime(),default=datetime.now,onupdate=datetime.now)
        )

orders=Table('orders',metadata,
        Column('order_id',Integer(),primary_key=True),
        Column('user_id',ForeignKey('users.user_id')),
        Column('shipped',Boolean(),default=False)
        )

line_tiesm=Table('line_items',metadata,
        Column('line_items_id',Integer(),primary_key=True),
        Column('order_id',ForeignKey('orders.order_id')),
        Column('cookie_id',ForeignKey('cookies.cookie_id')),
        Column('extened_cost',Numeric(12,2))
        )

engine = create_engine('sqlite:///:memory:')

connection = engine.connect(close_with_result=False)

metadata.create_all(engine)




ins=cookies.insert().values(
        cookie_name='chocolate chip',
        cookie_recipe_url="http://some.aweso.me/cookie/recipe.html",
        cookie_sku="CC01",
        quantity="12",
        unit_cost="0.50"
        )
print(str(ins))
print(ins.compile().params)

result = connection.execute(ins)
print(result.inserted_primary_key)

ins=cookies.insert()
result=connection.execute(
        ins,
        cookie_name='dark chocolate chip',
        cookie_recipe_url='http://some.awesomme/cookie/recipe_dark.html',
        cookie_sku='CC02',
        quantity='1',
        unit_cost='0.75'
        )
print(result.inserted_primary_key)

inventory_list=[
        {
            "cookie_name": 'peanut butter',
            'cookie_recipe_url': 'http://some.aweso.me/cookie/peanut.html',
            'cookie_sku': 'PB01',
            'quantity': '24',
            'unit_cost': '0.25'
            },
        {
            'cookie_name': 'oatmeal raisin',
            'cookie_recipe_url':'http://some.okay.me/cookie/raisin.html',
            'cookie_sku': 'EWW01',
            'quantity': '100',
            'unit_cost': '1.00'
            }
        ]

result=connection.execute(ins,inventory_list)

s=select([cookies])
rp=connection.execute(s)
results=rp.fetchall()
print(results)
