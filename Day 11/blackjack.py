import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_cards(player_or_comp):
    card = random.choice(cards)
    if (card == 11) and (sum(player_or_comp) > 21):
        card = 1

    player_or_comp.append(card)

def first_draw():
    global player_blackjack, comp_blackjack
    for _ in range(2):
        draw_cards(player_cards)
        draw_cards(comp_cards)

    if len(player_cards) == 2 and sum(player_cards) == 21:
        player_blackjack = True
    if len(comp_cards) == 2 and sum(comp_cards) == 21:
        comp_blackjack = True

def view_table():
    print(f"\nYour cards: {player_cards}, current score: {sum(player_cards)}")
    print(f"Computer's first card: {comp_cards[0]}")

def player_draw():
    while True:
        draw_flag = input("Type 'y' to get another card, type 'n' to pass: ")
        if(draw_flag == 'n'):
            break
        
        draw_cards(player_cards)
        if sum(player_cards) >= 21:
            break
        view_table()


def comp_draw():
    while True:
        if sum(comp_cards) <= 16:
            draw_cards(comp_cards)
        else:
            break

def final_hand():
    print(f"\nYour final hand: {player_cards}, final score: {sum(player_cards)}")
    print(f"Computer's final hand: {comp_cards}, final score {sum(comp_cards)}")

    if (sum(player_cards) == sum(comp_cards)):
        print("DRAW!")
    elif (player_blackjack == False) and (comp_blackjack == True):
        print("The computer has blackjack! You lose!")
    elif (player_blackjack == True) and (comp_blackjack == False):
        print("You have blackjack! You win!")
    elif (sum(player_cards) > 21) and (sum(comp_cards) <= 21):
        print("You went over 21! You lose!")
    elif (sum(player_cards) > 21) and (sum(comp_cards) > 21):
        print("You and the computer went over 21! You lose!")
    elif (sum(player_cards) <= 21) and (sum(comp_cards) > 21):
        print("Computer went over 21! You win!")  
    elif (sum(player_cards) < sum(comp_cards)):
        print("The computer had the higher hand! You lose!")
    elif (sum(player_cards) > sum(comp_cards)):
        print("You had the higher hand! You win!")

while True:
    player_cards = []
    comp_cards = []
    blackjack_flag = 0
    player_blackjack = False
    comp_blackjack = False

    play_flag = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play_flag == 'n':
        break
    print("\n" * 20)
    print(logo)

    first_draw()
    view_table()

    if(player_blackjack == False):
        player_draw()
    
    if(comp_blackjack == False):
        comp_draw()
    final_hand()
