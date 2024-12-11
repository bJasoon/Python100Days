print("Welcome to the rollercoaster?")
height = int(input("What is your height in cm?\n"))

if height >= 120:
    print("You can ride the rollercoaster")
else:
    print("You cannot ride the rollercoaster")


#========================================================

checkNum = int(input("What is your number?\n"))

if checkNum % 2 == 0:
    print(f"{checkNum} is even")
else:
    print(f"{checkNum} is odd")

#Shorter version
 
if int(input("What is your number?\n")) % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

#========================================================

print("Welcome to the rollercoaster?")
height = int(input("What is your height in cm?\n"))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?\n"))

    if age <= 12:
        print("Please pay $5")
    elif age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("You cannot ride the rollercoaster")

#========================================================

print("welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M or L\n")
pepperoni = input("Do you want pepperoni on your pizza? Y or N\n")
extra_cheese = input("Do you want extra cheese? Y or N\n")
total_bill = 0

if size == "S":
    total_bill += 15
    if pepperoni == "Y":
        total_bill += 2
elif size == "M":
    total_bill += 20
    if pepperoni == "Y":
        total_bill += 3
else:
    total_bill += 25
    if pepperoni == "Y":
        total_bill += 3

if extra_cheese == "Y":
    total_bill += 1

print(f"Your final bill is {total_bill}")

