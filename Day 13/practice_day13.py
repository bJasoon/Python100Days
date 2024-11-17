#try catch expressions

try:
    age = int(input("What is your age? "))
except ValueError:
    print("You have typed in an invalid input. Try a numerical input like 15")
    age = int(input("What is your age? "))

if age > 18:
    print(f"You can drive at age {age}")