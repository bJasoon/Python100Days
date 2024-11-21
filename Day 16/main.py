from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_on = True
coffee_menu = Menu()
coffee_maker = CoffeeMaker()
coffee_money = MoneyMachine()


while machine_on:
    drink_choice = input(f"What drink would you like? ({coffee_menu.get_items()}) ")
    match drink_choice: 
        case choice if choice in coffee_menu.get_items() and drink_choice != '':
            order = coffee_menu.find_drink(drink_choice)

            if coffee_maker.is_resource_sufficient(order) and coffee_money.make_payment(order.cost):
                coffee_maker.make_coffee(order)
            else:
                continue
            
        case 'report':
            coffee_maker.report()
            coffee_money.report()
        case 'off':
            print("Coffee machine is turning off. Goodbye!")
            machine_on = False
        case _:
            print("Please choose a valid input")
