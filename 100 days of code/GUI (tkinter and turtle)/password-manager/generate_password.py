import string
from random import choice, shuffle, randint


def password_generator():
    lowercase = list(string.ascii_lowercase)  # generate a list of lowercase characters in ascii
    uppercase = list(string.ascii_uppercase)  # generate a list of uppercase characters in ascii
    numbers = list(number for number in range(10))  # generate a list of numbers
    characters = list(c for c in (chr(i) for i in range(33, 48)))  # generate a list of the characters of ascii

    temp_password = []  # to store the generated characters, letters and numbers in the order of their generation
    password = ""  # to store the generated characters, letters and numbers string in a random order
    # generate the required number of lowercase,uppercase, numbers and characters
    # and store them in temp_password string

    temp_password += [choice(lowercase) for _ in range(randint(4, 6))]
    temp_password += [choice(uppercase) for _ in range(randint(4, 6))]
    temp_password += [str(choice(numbers)) for _ in range(randint(4, 6))]
    temp_password += [choice(characters) for _ in range(randint(3, 6))]
    shuffle(temp_password)  # shuffle the list
    password = password.join(temp_password)  # convert the shuffled list to a password string
    return password
