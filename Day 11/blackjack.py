import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
comp_cards = []

def get_cards():
    return random.choice(cards)

def draw_cards(player_or_comp):
    player_or_comp.append(get_cards())

def calculate_score(cards):
    return sum(cards)

def first_draw():
    for draw in range(2):
        draw_cards(player_cards)
        draw_cards(comp_cards)

player_score = 0
computer_score = 0

# play_flag = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
# print("\n" * 20)
# print(logo)

first_draw()
player_score = calculate_score(player_cards)
computer_score = calculate_score(comp_cards)

print(player_cards)
print(comp_cards)

print(f"Your cards: {player_cards}, current score: {player_score}")
print(f"Computer's first card: {comp_cards[0]}")

draw_player_flag = input("Type 'y' to get another card, type 'n' to pass: ")
