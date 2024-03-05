from art import logo
import os

print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_records):
    highest_bid = 0
    winner = ""
    for bidder in bidding_records:
        bid_amount = int(bidding_records[bidder])  # Convert bid amount to an integer
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest_bid}€")

# Function to clear the screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

while not bidding_finished:
    name = input("Enter your name: ")
    price = input("Enter the bid amount: €")
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()
