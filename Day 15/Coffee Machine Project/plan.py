MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

usa_coins ={
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01
}


profit = 0

# TODO: 1. Prompt user for what they would like
print(MENU['latte']['ingredients'])
user_prompt = input("What would you like? (espresso/latte/cappuccino/report): ").strip().lower()
print(MENU[user_prompt]['ingredients'])

# TODO: 2. If user enters 'report' return the report.

user_money = 0
def display_report():
    for key, item in resources.items():
        if key == 'coffee':
            print(f"{key}: {item}g")
        else:
            print(f"{key}: {item}ml")
    print(f"Money: ${user_money}")


# TODO: 3. If user asks for drink display price

def display_drink_price(drink:str) -> str:
        print(f"The price of an {drink} is ${MENU[drink]['cost']}")


# TODO: 4. Prompt user for quarters, dimes, nickles, and pennies


if user_prompt == "report":
    display_report()
elif user_prompt in ("espresso", "latte", "cappuccino"):
    display_drink_price(user_prompt)
    print("Please insert coins.")
    quarters = input("how many quarters?: ")
    dimes = input("how many dimes?: ")
    nickles = input("how many nickles?: ")
    pennies = input("How many pennies?: ")
elif user_prompt == "off":
    exit()

# TODO: 5. Calculate User Payment Total
coin_counts = []
coin_counts.extend([quarters, dimes, nickles, pennies])
coin_values = [0.25, 0.10, 0.05, 0.01]

    

def user_coins_total(coins: list[int]) -> float:
    sum = 0
    for i in range(len(coins)):
        sum += int(coin_counts[i])*coin_values[i]
    return round(sum, 2)
    ...
# TODO: 5.5. Total Owed
total_owed = MENU[user_prompt]['cost']

# TODO: 6. Calculate change

def payment_exchange(total_owed: float):
    total_payed = user_coins_total(coin_counts)
    if total_owed > total_payed:
        return "Sorry that's not enough money. Money refunded"
    elif total_owed < total_payed:
        return f"Here is ${round((total_payed-total_owed),2)} in change"
    else:
       profit += total_payed;
        
print(payment_exchange(total_owed))
# TODO: 7. Check resources sufficient

def total_ml_of_liquids(ingredients:dict) -> int:
    total = 0
    total += ingredients['water']
    total += ingredients['milk']
    return total


def sufficient_resources_check():
    drink_recipe =  MENU[user_prompt]['ingredients']
    resource_check = next((key for key, needed in drink_recipe.items() 
                          if needed > resources[key]), None)

    if resource_check:
        print(f"Sorry, we don't have {resource_check} to make a ${user_prompt}")



# TODO: 9. Expend resources to make Coffee




# TODO: 8. Connect All Coffee Machine Logic

# while True: 
    
#     if user_prompt == "report":
#         display_report()
#     elif user_prompt in ("espresso", "latte", "cappuccino"):
#         display_drink_price(user_prompt)
#         print("Please insert coins.")
#         quarters = input("how many quarters?: ")
#         dimes = input("how many dimes?: ")
#         nickles = input("how many nickles?: ")
#         pennies = input("How many pennies?: ")
#     elif user_prompt == "off":
#         exit()

print([resources])