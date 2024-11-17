import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of number between 1 and 100. Guess the number!")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

number = random.randint(1, 100)
lives = 0

if difficulty == 'easy':
    lives = 10
elif difficulty == 'hard':
    lives = 5

while True:
    if lives == 0:
        print(f"\n\nYou've run out of guesses. The number was {number}. You lose!")
        break
    
    print(f"\nYou have {lives} attempts reamining to guess the number")
    player_guess = int(input("Make a guess: "))

    if player_guess == number:
        print(f"\n\nYou got it! The number was {number}")
        break
    else:
        lives -= 1

    if player_guess < number and lives != 0:
        print("Too low\nGuess again")
    if player_guess > number and lives != 0:
        print("Too high\nGuess again")
    
        