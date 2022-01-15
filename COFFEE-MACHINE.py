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

while True:

    water = resources["water"]
    milk = resources["milk"]
    coffee_weight = resources["coffee"]
    money = 0


    def reporting():
        global coffee_name
        print(f'Water: {water}ml')
        print(f'Milk: {milk}ml')
        print(f'Coffee: {coffee_weight}g')
        print(f'Money: {money}')


    def remaining_and_insufficient_check():
        global water
        global milk
        global money
        global total
        global coffee_weight
        global coffee_name
        water -= MENU[coffee_name]['ingredients']['water']
        if coffee_name != 'espresso':
            milk -= MENU[coffee_name]['ingredients']['milk']
        coffee_weight -= MENU[coffee_name]['ingredients']['coffee']
        money += MENU[coffee_name]['cost']
        if total < money:
            print("Sorry! that's not enough money.Money refunded.")
        elif total >= money:
            if coffee_name == 'cappuccino':
                coffee_symbol = '🥤'
            elif coffee_name == 'latte':
                coffee_symbol = '🧋'
            elif coffee_name == 'espresso':
                coffee_symbol = '🍶'
            change = round(total - money, 2)
            print(f"Here is ${change} in change")
            print(f"Here is your {coffee_name}{coffee_symbol},Enjoy")


    def sufficiency():
        global loop
        global coffee_name
        if coffee_name != 'espresso' and water < MENU[coffee_name]['ingredients']['water']:
            if milk < MENU[coffee_name]['ingredients']['milk']:
                print("Sorry, milk and water are not sufficient")
                loop = False
            else:
                print("Sorry, water is not sufficient")
                loop = False
        elif water < MENU[coffee_name]['ingredients']['water']:
            print("Sorry, water is  not sufficient")
            loop = False
            if coffee_weight < MENU[coffee_name]['ingredients']['coffee']:
                print("and also coffee powder is not sufficient")


    coffee_name = input('What would you like? (espresso/latte/cappuccino) :')
    s = 0
    total = 0
    loop = True


    def coffee_machine():
        global s
        global total
        global coffee_name
        global loop
        while loop:
            if s == 1:
                coffee_name = input('What would you like? (espresso/latte/cappuccino) or '
                                    '"turnoff" to restart the machine:')
            while coffee_name != 'espresso' and coffee_name != 'latte' and coffee_name != 'cappuccino' and coffee_name != 'turnoff' and coffee_name != 'report':
                print("There is typo error,Please do type again from the given list")
                coffee_name = input('What would you like? (espresso/latte/cappuccino) or '
                                    '"turnoff" to restart the machine:')
            if coffee_name == 'turnoff':
                return 'turnoff'
            elif coffee_name == 'report':
                reporting()
            else:
                sufficiency()
                if loop:
                    print('Please insert coins.')
                    quarters = 0.25*int(input('how many quarters?: '))
                    dimes = 0.1*int(input('how many dimes?: '))
                    nickles = 0.05*int(input('how many nickles?: '))
                    pennies = 0.01*int(input('how many pennies?: '))
                    total = quarters + dimes + nickles + pennies
                    remaining_and_insufficient_check()
                else:
                    coffee_machine()
            s = 1
            loop = True


    y = True
    while y:
        if coffee_machine() == 'turnoff':
            y = False


















