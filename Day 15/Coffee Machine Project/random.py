
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

print(list(resources.items()))

print([(r,i) for r, i in resources.items()])

print(list(zip(resources.values())))

print(list(resources))

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    }}

customer = list(MENU["espresso"]['ingredients'].values())
print(customer)
me = list(resources.values())
print(me)

for limit, use in zip(me, customer):
    print(limit, use)
    print(limit - use)

