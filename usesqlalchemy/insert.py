from sqlalchemyUse import cookies
import sqlite3

con = sqlite3.connect("./orders.db")


ins = cookies.insert().values(
    cookie_name="chocolate chip",
    cookie_recipe_url="http://some.aweso.me/cookie/recipe.html",
    cookie_sku="CC01",
    quantity="12",
    unit_cost="0.50",
)
# con.execute(str(ins),ins.compile().params)
print(str(ins))
print(ins.compile().params)
