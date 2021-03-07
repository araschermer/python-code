import random


def pick_name():
    """select a random name from a list of names. The person selected will have to pay for everybody's food bill"""
    # Important: You are not allowed to use the choice() function.

    test_seed = int(input("create a seed number: "))
    random.seed(test_seed)
    names_string = input("enter everybody's names, separated by a comma. ")
    names = names_string.split(", ")
    if len(names) <= 1:
        print(f"only {names[0]} can buy the meal today")
    chosen_name = random.randint(0, len(names) - 1)
    print(f"{names[chosen_name]} is going to buy the meal today")


if __name__ == '__main__':
    pick_name()
