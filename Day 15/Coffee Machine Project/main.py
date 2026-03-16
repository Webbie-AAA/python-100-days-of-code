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

# TODO: 1. Prompt user for what they would like

user_prompt = input("What would you like? (espresso/latte/cappuccino/report): ").strip().lower()


# TODO: 2. If user enters 'report' return the report.

money = 0
def display_report():
    for key, item in resources.items():
        if key == 'coffee':
            print(f"{key}: {item}g")
        else:
            print(f"{key}: {item}ml")
    print(f"Money: ${money}")


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

# TODO: 5. Check resources sufficient

def total_ml_of_liquids(ingredients:dict) -> int:
    total = 0
    total += ingredients['water']
    total += ingredients['milk']
    return total


def sufficient_resources_check(drink):
    ...







