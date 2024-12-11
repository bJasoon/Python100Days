# Random module and importing/creating own modules
import random
import sample_module

random_int = random.randint(1,10)
print(random_int)

print(f"first 6 digits of pi {round(sample_module.pi_value_100, 6)}")

#===================================================
random_number_0to1 = random.random() * 10
print(random_number_0to1)

random_float = random.uniform(1, 10)
print(random_float)

#===================================================
# Heads or Tails (This code is overengineered)
# random_number = random.random() * 10

if input("Type heads or tails: ").lower() == "heads":
    if  -1 < (random_number_0to1) < 5:
        print(random_number_0to1)
        print("The coin landed heads. You win!")
    else:
        print(random_number_0to1)
        print("The coin landed tails. You lose!")
else:
    if  5 <= (random_number_0to1) < 10:
        print(random_number_0to1)
        print("The coin landed tails. You win!")
    else:
        print(random_number_0to1)
        print("The coin landed heads. You lose!")

#===================================================

#get a random int from 1 - 15 and display the number of digits of pi with the randint
random_digit = random.randint(1, 15)

print(f"The random number is {random_digit}")
print(f"The pi digit is {round(sample_module.pi,random.randint(1,15))}")

#===================================================

#Data Structures: Lists
states_of_america = ["Delaware", "Pennyslvania", "New Jersey", "Georgia"]

print(states_of_america)
print(states_of_america[2])
print(states_of_america[-1])
print(states_of_america[0])

states_of_america[0] = "Dela WERE"
print(states_of_america[0])

states_of_america.append("Texas")
print(states_of_america)

#===================================================
# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes"]

fruits = ["Strawberry", "Nectarines", "Apples", "Grapes"]
vegetables = ["Spinach", "Kale"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)

