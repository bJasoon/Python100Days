from data import MENU, resources

resources['money'] = 0
continue_serve = True

#======================================================
#Tesing Values
# resources["water"] = 100
# resources["milk"] = 100
# resources["coffee"] = 10
# print(resources["water"])
# print(resources["milk"])
# print(resources["coffee"])
#======================================================

# TODO 3.) Give report of current resources when entering "report" in coffee selection
def output_report(): # Need to refactor this as for loop seems inefficient
    '''This prints the list of ingredients remaining and the current revenue of the machine
       This has no inputs or outputs'''
    for report_item in resources:
        if(report_item == "water") or (report_item == "milk"):
            print(f"{report_item.title()}: {resources[report_item]}ml")
        elif (report_item == "money"):
            print(f"{report_item.title()}: ${round(resources[report_item],2)}")
        else:
            print(f"{report_item.title()}: {resources[report_item]}g")

# TODO 4.) When user chooses a drink, program must check if resources are sufficient and inform user
def has_resource(drink):
    '''This function receives the drink the user selects and returns True if there is sufficient
    ingredients for the drink or returns the ingredient that is missing for the drink. Order is based
    on the resources dictionary structure.'''
    
    
    for drink_ingredient in MENU[drink]["ingredients"]:
        if resources[drink_ingredient] < MENU[drink]["ingredients"][drink_ingredient]:
            return drink_ingredient
    return True

# TODO 5.) Prompt user to input coins if resources are sufficient
# The program must also get the input for each coin seperately and calculate how much they entered
# Penny = $0.01, Nickles = $0.05, Dimes = $0.10, Quarters = $0.25
def process_coins(drink):
    '''This function receives the drink choice of the user. It will then prompt the user to input their coins
    based on quarters, dimes, nickles and pennies. It will calculate the amount of money based on the inputted 
    coins and check if the amount is enough to cover the cost of the drink. If the money is enough, it will add
    the cost of the drink to the machine revenue and calculate the change that is to be given to the user as this
    function's output. If not, the function will return -1 as indication that the user does not have enough money'''


    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    amount = round(((quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)),2)
# TODO 6.) Check if transaction is successful. Check if enough money has been provided by user to 
# purchase the drink they selected. If insufficient coins, inform user that it is not enough and refund money
# If user has enough money, the cost of drink is added to machine profit and reflected once report is triggered again
# If user has too much money, provide change and input amount. change is rounded up 2 decimal places
    if amount >= MENU[drink]['cost']:
        resources["money"] += MENU[drink]['cost']
        amount -= MENU[drink]['cost']
        return amount
    else:
        return -1

# TODO 7.) If transaction is successful, the ingredients must be deducted from how much the machine currently has

def deduct_resources(drink):
    '''This function receives the drink choice as parameters. It will deduct the resources based on the drink chosen
    It will then print a statement informing the user of their drink and to enjoy it.'''
    for drink_ingredient in MENU[drink]["ingredients"]:
        resources[drink_ingredient] -= MENU[drink]["ingredients"][drink_ingredient]
# Once ingredients are deducted, tell user to enjoy their drink.
    print(f"Here is your {drink}. Enjoy!")

# TODO 1.) Prompt user to choose what coffee they would like
while continue_serve:
    drink_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    match drink_choice:
        case 'espresso' | 'latte' | 'cappuccino':
            check_resource = has_resource(drink_choice)
            user_coins = 0

            if check_resource != True:
                print(f"Sorry, there is not enough {check_resource}.")
                continue
            
            user_coins = process_coins(drink_choice)
            if user_coins == -1:
                print("Sorry, that's not enough money. Money refunded.")
                continue
            else:
                print(f"Here is ${round(user_coins,2)} in change.")
                deduct_resources(drink_choice)           
        case 'report':
            output_report()
        case 'off': # TODO 2.) Turn off coffee machine when entering off in coffee selection
            print("Coffee machine is turning off. Goodbye!")
            continue_serve = False
        case _:
            print("Please choose a valid input")

 