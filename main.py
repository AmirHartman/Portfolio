from Data import MENU
import math

resources = {
    'water': 1000,
    'milk': 500,
    'coffee': 200,
    'money': 0
}


def report():
    print("The machine contains:")
    print(f"water: {resources['water']}ml")
    print(f"milk: {resources['milk']}ml")
    print(f"coffee: {resources['coffee']}g")
    print(f"money: {resources['money']}$")


def check_resources_sufficient(drink):
    """checks if there is enough resources to make the drink.
    if do, returns 'enough'
    if not: prints what is missing and returns 'not enough'"""
    result = 'enough'
    for ingredient_checked in MENU[drink]['ingredients']:
        if MENU[drink]['ingredients'][ingredient_checked] > resources[ingredient_checked]:
            print(f"Sorry there is not enough {ingredient_checked} to make this drink.")
            result = 'not enough'
        else:
            return result


def process_coins():
    money_inserted = 0
    print("Insert coins: ")
    money_inserted += int(input("How many quarters do you want to enter?: ")) * 0.25
    money_inserted += int(input("How many dimes do you want to enter?: ")) * 0.1
    money_inserted += int(input("How many nickles do you want to enter?: ")) * 0.05
    money_inserted += int(input("How many pennies do you want to enter?: ")) * 0.01
    return money_inserted


users_pick = ''

while users_pick != 'off':
    users_pick = input("“What would you like? (espresso/latte/cappuccino): ").lower()
    if users_pick == 'report':
        report()
    elif users_pick == 'off':
        print("Machine turned off successfully")
    elif users_pick in MENU:
        if check_resources_sufficient(users_pick) == 'enough':
            user_money = process_coins()
            if user_money >= MENU[users_pick]['cost']:
                resources['money'] += MENU[users_pick]['cost']
                # subtract used ingredients from resources
                for ingredient in MENU[users_pick]['ingredients']:
                    resources[ingredient] -= MENU[users_pick]['ingredients'][ingredient]
                change = user_money - MENU[users_pick]['cost']
                change = math.floor(change * 100) / 100
                if change > 0:
                    print(f"Here is ${change} in change")
                print(f"Here is your {users_pick}. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
    else:
        print("Invalid input!")
