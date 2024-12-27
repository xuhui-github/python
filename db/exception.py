from datetime import datetime
from sqlalchemy import (
    MetaData,
    Table,
    Column,
    Integer,
    Numeric,
    String,
    DateTime,
    ForeignKey,
    Boolean,
    create_engine,
    CheckConstraint,
)
from sqlalchemy.exc import IntegrityError

metadata = MetaData()
cookies = Table(
    "cookies",
    metadata,
    Column("cookie_id", Integer(), primary_key=True),
    Column("cookie_name", String(50), index=True),
    Column("cookie_recipe_url", String(255)),
    Column("cookie_sku", Integer()),
    Column("quantity", Integer()),
    Column("unit_cost", Numeric(12, 2)),
    CheckConstraint("quantity > 0", name="quantity_positive"),
)
users = Table(
    "users",
    metadata,
    Column("user_id", Integer(), primary_key=True),
    Column("username", String(15), nullable=False, unique=True),
    Column("email_address", String(255), nullable=False),
    Column("phone", String(20), nullable=False),
    Column("password", String(25), nullable=False),
    Column("created_on", DateTime(), default=datetime.now),
    Column("updated_on", DateTime(), default=datetime.now, onupdate=datetime.now),
)

orders = Table(
    "orders",
    metadata,
    Column("order_id", Integer(), primary_key=True),
    Column("user_id", ForeignKey("users.user_id")),
    Column("shipped", Boolean(), default=False),
)

line_items = Table(
    "line_items",
    metadata,
    Column("line_items_id", Integer(), primary_key=True),
    Column("order_id", ForeignKey("orders.order_id")),
    Column("cookie_id", ForeignKey("cookies.cookie_id")),
    Column("quantity", Integer()),
    Column("extended_cost", Numeric(12, 2)),
)

# engine=create_engine('sqlite:///:memory:')
engine = create_engine("postgresql://xuhui:flower@localhost:5432/postgres")
metadata.create_all(engine)
connection = engine.connect()


from sqlalchemy import insert, select

ins = insert(users).values(
    username="cookiemon",
    email_address="mon@cookie.com",
    phone="111-111-1111",
    password="password",
)

try:
    results = connection.execute(ins)
except IntegrityError as error:
    print(error.orig, error.params)
for result in results:
    print(result.username)
    print(result.password)
