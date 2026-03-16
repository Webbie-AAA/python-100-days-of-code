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

user_prompt = input("What would you like? (espresso/latte/cappuccino/report): ")

# TODO: 2. If user enters 'report' return the report.

money = 0
def display_report():
    for key, item in resources.items():
        if key == 'coffee':
            print(f"{key}: {item}g")
        else:
            print(f"{key}: {item}ml")
    print(f"Money: ${money}")

display_report()

