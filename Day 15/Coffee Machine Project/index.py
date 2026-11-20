from menu import MENU, resources

my_profit = {'money': 0}

def income(profit):
     my_profit['money'] = my_profit['money'] + profit
     print(my_profit['money'])

def display_report():
    for key, item in resources.items():
        if key == 'coffee':
            print(f"{key}: {item}g")
        else:
            print(f"{key}: {item}ml")
    print(f"Money: ${my_profit['money']}")


def display_drink_price(drink:str) -> str:
        print(f"The price of an {drink} is ${MENU[drink]['cost']}")


def user_coins_total(coins: list[int]) -> float:
    coin_values = [0.25, 0.10, 0.05, 0.01]
    sum = 0
    for i in range(len(coins)):
        sum += int(coin_counts[i])*coin_values[i]
    return round(sum, 2)


def payment_exchange(total_owed: float):
    profit = 0
    total_payed = user_coins_total(coin_counts)
    if total_owed > total_payed:
        return "Sorry that's not enough money. Money refunded"
    elif total_owed < total_payed:
        profit = round((total_payed-total_owed),2)
        income(profit)
        return f"Here is ${profit} in change"


def deduct_resources_after_sell(coffee_sold: str) -> list:
    resources_deducted = [] 
    usage = list(MENU[coffee_sold]['ingredients'].values())
    limit = list(resources.values())
    for lim, use in zip(limit, usage):
        resources_deducted.append(lim - use)
        print(resources_deducted)
    return resources_deducted


def updated_resources(deducted_resources: list) -> dict:
    if len(deducted_resources) >= 2:
        resources['water'] = deducted_resources[0]
        resources['coffee'] = deducted_resources[1]
        if len(deducted_resources) == 3:
             resources['milk'] == deducted_resources[2]
    return resources
            
    
         
def sufficient_resources_check():
    drink_recipe =  MENU[user_prompt]['ingredients']
    resource_check = next((key for key, needed in drink_recipe.items() 
                          if needed > resources[key]), None)

    if resource_check:
        print(f"Sorry, we don't have {resource_check} to make a ${user_prompt}")

         

while True: 
    user_prompt = input("What would you like? (espresso/latte/cappuccino/report): ").strip().lower()
    if user_prompt == "report":
            display_report()
    elif user_prompt in ("espresso", "latte", "cappuccino"):
            display_drink_price(user_prompt)
            sufficient_resources_check
            total_owed = MENU[user_prompt]['cost']
            print("Please insert coins.")
            quarters = input("how many quarters?: ")
            dimes = input("how many dimes?: ")
            nickles = input("how many nickles?: ")
            pennies = input("How many pennies?: ")


            coin_counts = []
            coin_counts.extend([quarters, dimes, nickles, pennies])
            

            user_coins_total(coin_counts)
            print(payment_exchange(total_owed))
            deducted_resources = deduct_resources_after_sell(user_prompt)
            updated_resources(deducted_resources)
    elif user_prompt == 'off':
         exit()


            
            