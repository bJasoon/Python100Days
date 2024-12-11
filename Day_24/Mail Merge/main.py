#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names = []
letter = []
added_name = []

with open ("./Input/Names/invited_names.txt", "r") as names_file:
    for line in names_file.readlines():
        names.append(line.removesuffix("\n"))

with open("./Input/Letters/starting_letter.txt", "r") as letter_format:
    letter = letter_format.readlines()

#both ^ and v code can be combined
#TODO refactor

for name in names:
    edited_name = letter[0].replace("[name]", name)
    with open(f"./Output/ReadyToSend/letter_to_{name}.txt", "w")as final_letter:
        final_letter.write(edited_name)
        final_letter.writelines(letter[1:])
