#Silent Auction
import os
def bid_winner(bidder_details):
    high_bid=0
    winner=""
    for bid in bidder_details:
        bid_price=bidder_details[bid]
        if bid_price>high_bid:
            bid_price = high_bid
            winner=bid
    print(f"The winner is {winner} with a bid of {high_bid}")
wanna_do=False
bidd ={}
while not wanna_do:
    name=input("Enter bidder name: ")
    price = float(input("Enter price: "))
    bidd[name]=price
    quit=input("Enter yes to quit or no to continue: ").lower()
    if quit=="yes":
        wanna_do=True
        bid_winner(bidd)
    elif quit=="no":
        os.system('cls')


