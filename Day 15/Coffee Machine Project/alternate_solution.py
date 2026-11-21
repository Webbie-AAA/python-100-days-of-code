from menu import MENU, resources
profit = 0

is_on = True


def is_resource_sufficient(order_ingredients):
    """Returns True or False based on whether enough resources are available to make order"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f'sorry there is not enough {item}')
            return False
        return True


def process_coins():
    """Returns the total calculated from coins inserted"""
    print('please insert coins.')
    total = int(input("how many quarters: ")) * 0.25
    total += int(input("how many dimes: ")) * 0.1
    total += int(input("how many nickles: ")) * 0.05
    total += int(input("how many pennies: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Returns True when payment is accepted, or False"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f'Here is ${change} in change')
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False
    ...


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️")


while is_on:
    choice = input('What would you like? (espresso/latte/cappuccino): ')
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        [print(f"{k} : {v}") for k, v in resources.items()]
        print(f"profit: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])
