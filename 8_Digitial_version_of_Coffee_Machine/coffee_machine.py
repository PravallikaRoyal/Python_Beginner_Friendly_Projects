#storing menu in dictionary
profit = 0
menu = {
    "espresso" : {
           "ingredients" : {
               "water" : 50,
               "milk" : 18
           },
           "cost" : 1.5,
    },
    "Latte" : {
        "ingredients" : {
            "water" : 50,
            "milk" : 100,
            "coffee" : 24
        },
        "cost" : 2.5
    },
    "cappichuno" : {
        "ingredients" : {
            "water" : 100,
            "milk" : 250,
            "coffee" : 24
        },
        "cost" : 3.0
    }
}

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
        
    return True

def process_coins(drink_cost):
    print(f"The cost of your drink is {drink_cost}")
    print(f"Please insert coins accordingly to the {drink_cost}")
    total = int(input("How many quarters $(0.25) ?") )* 0.25
    total += int(input("How many dimes $(0.10) ?")) * 0.10
    total += int(input("How many nickles $(0.05) ?"))* 0.05
    total += int(input("How many pennies $ (0.01) ?")) * 0.01
    print(f"Total amount inserted: ${round(total,2)}")
    return total

def is_transcaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"Here is {change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print(" Sorry Money received isn't enough, try again")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕ Enjoy!")


resources = {"water" : 300, "coffee" : 100, "milk" : 200}
is_on = True
while is_on : 
    choice = input("What would you like to have? (Espresso, latte, cappucino)")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water : {resources["water"]} ml")
        print(f"milk : {resources["milk"]} ml" )
        print(f"coffee : {resources["coffee"]} g")
        print(f"Profit : ${profit}")
    else:
        drink = menu[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins(drink["cost"])
            if is_transcaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])


