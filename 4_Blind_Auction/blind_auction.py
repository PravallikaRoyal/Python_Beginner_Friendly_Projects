def find_highest_bidder(bids):
    highest_bid = 0
    winner = ""
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with bid of ${highest_bid}" )

bid = {}
continue_bidding = True
while continue_bidding:
    name = input("Enter your name:")
    price = int(input("Enter the amount you want to bid: $"))
    bid[name] = price
    should_continue = input("Are there any bidders? type yes or no:")
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bid)
    elif should_continue == "yes":
        print("\n "* 20)

