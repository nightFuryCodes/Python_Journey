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
            "milk": 350,
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

money = 0

def showResources():
    print(f'''
Water : {resources["water"]}ml
Milk : {resources["milk"]}ml
Coffee : {resources["coffee"]}g
Money : ${money}
''')

def coin_calculator(coffee):
    print("Please insert coins.")
    quarter = int(input("How many quarters?: "))
    quarter *= 0.25
    dime = int(input("How many dimes?: "))
    dime *= 0.10
    nickle = int(input("How many nickles?: "))
    nickle *= 0.05
    penny = int(input("How many pennies?: "))
    penny *= 0.01
    amount = quarter + dime + nickle + penny
    print(f"You entered {amount} dollars.")
    if amount < MENU[coffee]["cost"]:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    elif amount >= MENU[coffee]["cost"]:
        change = round(amount - MENU[coffee]['cost'], 2)
        print(f"Here is ${change} in change")
        global money
        money += MENU[coffee]["cost"]
        return True

def used_resources(coffee_ingredients):
    for item in coffee_ingredients:
        resources[item] -= coffee_ingredients[item]


def check_resources(coffee_ingredients):
    for item in coffee_ingredients:
        if coffee_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True


def coffee_machine():
    coffee = input("What would you like? (espresso/latte/cappuccino): ")
    if coffee == "off":
        return
    elif coffee == "report":
        showResources()
        coffee_machine()
    elif coffee == "espresso" or coffee == "latte" or coffee == "cappuccino":
        if check_resources(MENU[coffee]["ingredients"]) :
            if coin_calculator(coffee):
                print(f"Here is your {coffee}. Enjoy!")
                used_resources(MENU[coffee]["ingredients"])
                coffee_machine()
            else:
                coffee_machine()
        else:
            coffee_machine()
    else:
        print("Invalid response! Please try again.")
        coffee_machine()

coffee_machine()



