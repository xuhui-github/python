from sqlalchemyUse import cookies
import sqlite3

con = sqlite3.connect("./orders.db")


ins = cookies.insert().values(
        cookie_name="chocolate chip",
        cookie_recipe_url="http://some.aweso.me/cookie/recipe.html",
        cookie_sku="CC01",
        quantity="12",
        unit_cost="0.50"
        )
con.execute(str(ins),ins.compile().params)
print("-----------")
print(ins.values())
print(ins.compile().params.values())
result=con.execute(str(ins),tuple(ins.compile().params.values()))
print(result.rowcount)
print("--------")
print(str(ins))
print(ins.compile().params)
print("------------->")
#result=con.execute(str(ins))
result= con.execute(str(ins),ins.compile().params)

ins1 = cookies.insert()
#result = con.execute(
#        ins,
#        cookie_name='dark chocolate chip',
#        cookie_recipe_url='http://some.aweso.me/cookie/recipe_dark.html',
#        cookie_sku='CC02',
#        quantity='1',
#        unit_cost='0.75'
#        )
#print(result.inserted_primary_key)
#
#print("--------------->")
#
#
#ins1 = cookies.insert()
#print("*******")
#print(str(ins))
print(str(ins1))
inventory_list = [
        {
            'cookie_name': 'peanut butter',
            'cookie_recipe_url': 'http://some.aweso.me/cookie/peanut.html',
            'cookie_sku': 'PB01',
            'quantity': '24',
            'unit_cost': '0.25'
            },
        {
            'cookie_name': 'oatmeal raisin',
            'cookie_recipe_url': 'http://some.okay.me/cookie/raisin.html',
            'cookie_sku': 'EWW01',
            'quantity': '100',
            'unit_cost': '1.00'
            }
        ]
result = con.executemany(str(ins), inventory_list)
#result= con.executemany(str(ins),[item.values() for item in inventory_list])
#cur = con.cursor()
#result = cur.executemany(str(ins),inventory_list)
con.commit()

