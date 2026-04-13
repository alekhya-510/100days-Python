import art
print(art.logo)

# TODO-1: Ask the user for input


# TODO-2: Save data into dictionary {name: price}
# TODO-4: Compare bids in dictionary
def highest_bidder(bidding_dictionary):
    winner= ""
    highest_bid= 0
    for bid in bidding_dictionary:
        bid_amount=bidding_dictionary[bid]
        if bid_amount > highest_bid:
            highest_bid= bid_amount
            winner= bid
    print(f"The winner is {winner} with highest bid of ${highest_bid}")



# TODO-3: Whether if new bids need to be added
auction_data= {}
continue_bid = True
while continue_bid:
    name=  input("What is your name?")
    price= int(input("What is your bid ?: $"))
    auction_data[name] = price
    prompt = input("Are there any other bidders? Type 'yes' or 'no \n").lower()
    if prompt == "yes":
        print("\n" * 100)
    elif prompt == "no":
        continue_bid = False
        highest_bidder(auction_data)

