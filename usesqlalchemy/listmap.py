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
for item in inventory_list:
    print(tuple(item.values()))

items = [tuple(item.values()) for item in inventory_list]
print(items)
