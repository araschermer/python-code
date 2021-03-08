logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


def do_auction(bidder, bid, auction):  # to print multiple bidders out, in case of bidding the same bid amount
    auction[bidder] = bid
    highest_bid_ = max(auction.values())
    highest_bidder = [name for name, value in auction.items() if value == highest_bid_]
    return highest_bidder


# Alternative function to announce only a single bidder and multiple equal winning bids
def highest_bid(bidder, bid, auction):
    auction[bidder] = bid
    highest_bid_ = 0
    highest_bidder = ""
    for bidder in auction:
        bid_amount = auction[bidder]
        if bid_amount > highest_bid_:
            highest_bidder = bidder
            highest_bid_ = bid_amount
    return highest_bid_, highest_bidder


def start_auction(stop):
    """Start blind auction.
    for a better visual of the functionality
     check: https://repl.it/@abdelkha/blind-auction?embed=1&output=1#main.py """
    auction = {}
    print(logo)
    while not stop:
        bidder = input("please enter your name\n").title()
        bid = int(input("please enter your bid\n"))
        more_bids = input("are there any other bidders type yes to continue, no to announce the winner\n").lower()
        if more_bids == "no":
            stop = True
            highest_bid_, highest_bidder = highest_bid(bidder, bid, auction)

            print(f"the winner is: {highest_bidder} with a bid of: ${highest_bid_}")

        else:
            highest_bid(bidder, bid, auction)


if __name__ == "__main__":
    start_auction(stop = False)
