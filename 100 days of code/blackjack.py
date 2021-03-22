import random

logo = """
    .------.            _     _            _    _            _    
    |A_  _ |.          | |   | |          | |  (_)          | |   
    |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
    | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
    `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
          |  \/ K|                            _/ |                
          `------'                           |__/           
    """


# If the computer and user both have the same score, then it's a draw.
# If the computer has a blackjack (0), then the user loses.
# If the user has a blackjack (0), then the user wins.
# If the user_score is over 21, then the user loses.
# If the computer_score is over 21, then the computer loses.
# If none of the above, then the player with the highest score wins.
def compare(user_score, computer_score):
    # Bug fix. If you and the computer are both over, you lose.
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.
def calculate_score(cards):
    """Take a list of cards, sums the cards and return the score."""
    # check for a blackjack (a hand with only 2 cards: ace + 10) and return 0
    # instead of the actual score. 0 will represent a blackjack in our game.
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # check for an 11 (ace). If the score is already over 21, remove the 11 and
    # replace it with a 1. You might need to look up append() and remove().
    return ace_check(cards)


def ace_check(cards):
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def play_game():
    """for a better visual of the functionality
     check: https://repl.it/@abdelkha/blackjack?embed=1&output=1#main.py
    """
    print(f"\n \n {logo}\n")
    # Deal the user and computer 2 cards each using deal_card()
    user_cards = []
    computer_cards = []
    is_game_over = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    # The score will need to be rechecked with every new card drawn.

    while not is_game_over:
        # If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes,
            # then use the deal_card() function to add another card to the user_cards List. If no, then the game has
            # ended.
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
    # Once the user is done, it's time to let the computer play. The computer should keep drawing cards as
    # long as it has a score less than 17.
    user_score = sum(user_cards)
    computer_score = sum(computer_cards)
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score} \n \n ")
    print(compare(user_score, computer_score))


if __name__ == "__main__":
    again = True
    while again:
        play_game()
        play_again = input("\nplay again? Type 'y' to play again, 'no' to quit\n").lower()
        if play_again == "no":
            again = False
        else:
            again = True
