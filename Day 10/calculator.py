from calc_art import logo

def add(n1, n2):
    return n1+n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2

def input_first_num():
    return float(input("What is the first number?: "))

def input_op():
    for symbol in operations:
        print(symbol)
    return str(input("Pick an operation: "))

def input_second_num():
    return float(input("what is the second number?: "))

def input_continue():
    return input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()

operations = {
    "+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide
}

while True:
    print(logo)
    first_num = input_first_num()
    op = input_op()
    second_num = input_second_num()

    result = operations[op](first_num,second_num)

    print(f'{first_num} {op} {second_num} is equal to {result}')

    continue_prompt = input_continue()
    while continue_prompt == 'y':
        first_num = result
        op = input_op()
        second_num = input_second_num()
        result = operations[op](first_num,second_num)

        print(f'{first_num} {op} {second_num} is equal to {result}')

        continue_prompt = input_continue()