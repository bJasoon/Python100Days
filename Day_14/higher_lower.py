import random
from art import logo, vs
from game_data import data

compareA = random.choice(data)
compareB = random.choice(data)
fail_flag = False
player_score = 0

def is_correct(choice):
    if choice == 'A':
        if compareA["follower_count"] > compareB["follower_count"]:
            return True
        else:
            return False
    else:
        if compareA["follower_count"] < compareB["follower_count"]:
            return True
        else:
            return False

def view_comparison():
    check_score()
    print(f'Compare A: {compareA["name"]}, a {compareA["description"]}, from {compareA["country"]}')
    print(f"\n{vs}\n")
    print(f'Against B: {compareB["name"]}, a {compareB["description"]}, from {compareB["country"]}')

def check_score():
    if player_score != 0:
        print(f"You're right! Current score: {player_score}")

def print_logo():
    print("\n" * 20)
    print(logo)

while True:
    print_logo()

    view_comparison()
    player_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    if is_correct(player_choice) == False:
        print_logo()
        print(f"Sorry, that's wrong. Final score: {player_score}")
        break
    else:
        compareA = compareB
        player_score += 1
        compareB = random.choice(data)
