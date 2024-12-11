from gavel_art import logo

def initialize():
    print(logo)
    print("Welcome to the secret auction program.")

def determine_winner():
    current_highest = ""
    highest_bid = 0
    # You can use the max() function to determine the highest value in a dictionary
    for check_winner in bidders_and_bids:
        if bidders_and_bids[check_winner] > highest_bid:
            current_highest = check_winner
            highest_bid = bidders_and_bids[check_winner]
    return current_highest

initialize()
bidders_and_bids = {}
add_more = True

while add_more:
    bidder_name = input("What is your name?: ")
    bid_amount = int(input("What is your bid?: $"))
    add_more_prompt = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    bidders_and_bids[bidder_name] = bid_amount

    if add_more_prompt == "no":
        add_more = False
    print("\n" * 20)

winner = determine_winner()
print(f"The winner of the auction is {winner} with a bid of ${bidders_and_bids[winner]}!")
    
