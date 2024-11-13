import random
import hangman_ascii
import hangman_words

display = ""
progress = []
lives = 6

chosen_word = random.choice(hangman_words.word_list)
print(hangman_ascii.logo)

for blank in range(len(chosen_word)):
    display += "_"
    progress.append("_")

print(display)

while ("_" in display) and (lives != 0):
    correct_flag = 0
    index = 0

    guess = (input("Guess a letter: ")).lower()
    
    for letter_in_chosen in chosen_word:
        if (letter_in_chosen == guess) and (progress[index] == "_"):
            progress[index] = letter_in_chosen
            correct_flag = 1
        index += 1

    if correct_flag == 0:
        if guess in progress:
            print(f"You already guessed the letter {guess}.")
        else:
            print(f"The letter {guess} is not in the word. You lose a life.")
            lives -= 1

    
    display = "".join(progress)
    print(display)
    print(hangman_ascii.HANGMANPICS[lives])
    print(f"****************************{lives} LIVES LEFT****************************")


if lives != 0:
    print("You win")
else:
    print(f"You lose\nThe correct word was {chosen_word}")

    