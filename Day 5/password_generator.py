#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
allchar = [letters,numbers,symbols]

# leters = 52, numbers 10, symbols 9

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

generatedPassword = []
checkLetterLimit = 1
checkSymbolLimit = 1
checkNumberLimit = 1

for currentIteration in range(0, nr_letters+nr_symbols+nr_numbers):
    chooseCharType = random.randint(0,2)

    if chooseCharType == 0:
        if checkLetterLimit >= nr_letters:
            if checkNumberLimit >= nr_numbers:
                generatedPassword.append(random.choice(symbols))
                checkSymbolLimit += 1
            else:
                generatedPassword.append(random.choice(numbers))
                checkNumberLimit += 1
        else:
            generatedPassword.append(random.choice(letters))
            checkLetterLimit += 1
        

    elif chooseCharType == 1:
        if checkNumberLimit >= nr_numbers:
            if checkLetterLimit >= nr_letters:
                generatedPassword.append(random.choice(symbols))
                checkSymbolLimit += 1
            else:
                generatedPassword.append(random.choice(letters))
                checkLetterLimit += 1
        else:
            generatedPassword.append(random.choice(numbers))
            checkNumberLimit += 1

    elif chooseCharType == 2:
        if checkSymbolLimit >= nr_symbols:
            if checkLetterLimit >= nr_letters:
                generatedPassword.append(random.choice(numbers))
                checkNumberLimit += 1
            else:
                generatedPassword.append(random.choice(letters))
                checkLetterLimit += 1
        else:    
            generatedPassword.append(random.choice(symbols))
            checkSymbolLimit += 1

    
print(f'Your generated password is {"".join(generatedPassword)}')

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# for currentIteration in range(0, num_of_characters_in_pw):
#     chooseCharType = random.randint(0,2)
#     if chooseCharType == 0 and checkLetterLimit < nr_letters:
#         chooseChar = random.randint(0,51)
#         generatedPassword.append(letters[chooseChar])
#         checkLetterLimit += 1
#     elif chooseCharType == 1 and checkNumberLimit < nr_numbers:
#         chooseChar = random.randint(0,9)
#         generatedPassword.append(numbers[chooseChar])
#         checkSymbolLimit += 1
#     elif chooseCharType == 2 and checkSymbolLimit < nr_symbols:
#         chooseChar = random.randint(0,8)
#         generatedPassword.append(symbols[chooseChar])
#         checkNumberLimit += 1
#     else:
#         currentIteration -= 1