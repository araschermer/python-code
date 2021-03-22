import random


def rock_paper_scissors_lizard_spock():
    """
    Rock crushes Lizard and crushes Scissors
    Paper disproves Spock and covers Rock
    Scissors decapitates Lizard and cuts Paper
    Lizard poisons Spock and eats Paper
    Spock smashes Scissors and vaporizes Rock"""
    rock = '''
          _______
      ---'   ____)
            (_____)
            (_____)
            (____)
      ---.__(___)
      '''

    paper = '''
          _______
      ---'   ____)____
                ______)
                _______)
               _______)
      ---.__________)
      '''

    scissors = '''
          _______
      ---'   ____)____
                ______)
             __________)
            (____)
      ---.__(___)
      '''
    spock = """░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░▄▄▄░▄▄▄░░░▄▄▄░▄▄▄
░░░░░░░░░░█░░░█░░░█░█░░░█░░░█
░░░░░░░░░█░░░░█░░░█░█░░░█░░░█
░░░░░░░░░█░░░█░░░█░█░░░█░░░█
░░░░░░░░░█░░░█░░░█░█░░░█░░░█
░░░░░░░░░█░░░█░░░█░█░░░█░░░█
░░░░░░░░░█░░░█░░░█░█░░░█░░░█
░░░░░░▄▄▄█░░░█░░░█▄█░░░█░░░█
░░░░░█░░░░█░░░░░░░░░░░░░░░░█
░░░░░█░░░░░█░░░░░░░░░░░░░░░░█
░░░░░█░░░░░█░░░░░░░░░░░░░░░░█
░░░░░█░░░░█░░░░░░░░░░░░░░░░░█
░░░░░█░░░░█░░░░░░░░░░░░░░░░░█
░░░░░█░░░░░█░░░░░░░░░░░░░░░░█
░░░░░█░░░░░░░░░░░░░░░░░░░░░░█
░░░░░░█░░░░░░░░░░░░░░░░░░░░█
░░░░░░░█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
░░░░░░░█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
░░░░░░████████████████████"""
    lizard = """    _.-~~-.__
 _-~ _-=-_   ''-,,
('___ ~~~   0     ~''-_,,,,,,,,,,,,,,,,
 \~~~~~~--'                            '''''''--,,,,
  ~`-,_      ()                                     '''',,,
       '-,_      \                           /             '', _~/|
  ,.       \||/~--\ \_________              / /______...---.  ;  /
  \ ~~~~~~~~~~~~~  \ )~~------~`~~~~~~~~~~~( /----         /,'/ /
   |   -           / /                      \ \           /;/  /
  / -             / /                        / \         /;/  / -.
 /         __.---/  \__                     /, /|       |:|    \  \
/_.~`-----~      \.  \ ~~~~~~~~~~~~~---~`---\\\\ \---__ \:\    /  /
                  `\\\`                     ' \\' '    --\'\, /  /
                                               '\,        ~-_'''\n"""

    game_images = [rock, paper, scissors, lizard, spock]
    print("welcome to the Rock Paper Scissors Lizard Spock game!\n")
    print(" the rules of the game are:")
    game_rules = """
    Rock crushes Lizard and crushes Scissors
    Paper disproves Spock and covers Rock
    Scissors decapitates Lizard and cuts Paper
    Lizard poisons Spock and eats Paper
    Spock smashes Scissors and vaporizes Rock\n """
    print(game_rules)
    play = 1

    while play:
        user_choice = input("What do you choose? Type 1 for Rock, 2 for Paper, 3 for Scissors, 4 for Lizard, "
                            "or 5 for spock!, Type X to quit, or R for the game rules!\n").lower()
        if "x" in user_choice:
            print("See you again soon!")
            break
        elif "r" in user_choice:
            print(game_rules)
            continue
        else:
            user_choice = int(user_choice)

        print(f"Your choice is:\n {game_images[user_choice - 1]}")
        computer_choice = random.randint(1, 5)
        print("Computer chose:")
        print(game_images[computer_choice - 1])
        if user_choice >= 6 or user_choice <= 0:
            print("You typed an invalid number, you lose!")
        elif computer_choice == user_choice:
            print("It's a draw")
        elif user_choice == 1 and computer_choice in [3, 4]:
            user_wins()
        elif user_choice == 2 and computer_choice in [1, 5]:
            user_wins()
        elif user_choice == 3 and computer_choice in [2, 4]:
            user_wins()
        elif user_choice == 4 and computer_choice in [2, 5]:
            user_wins()
        elif user_choice == 5 and computer_choice in [1, 3]:
            user_wins()
        else:
            print("You lose")


def user_wins():
    print("You won!")


if __name__ == '__main__':
    rock_paper_scissors_lizard_spock()

#     Rock[1] crushes Lizard[4] and crushes Scissors[3]
#     Paper[2] disproves Spock[5] and covers Rock[1]
#     Scissors[3] decapitates Lizard[4] and cuts Paper[2]
#     Lizard[4] poisons Spock[5] and eats Paper[2]
#     Spock[5] smashes Scissors[3]and vaporizes Rock[1]"""
