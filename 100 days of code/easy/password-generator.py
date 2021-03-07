import string
from random import choice, shuffle


def password_generator(num_lowercase=-1, num_uppercase=-1, num_numbers=-1, num_characters=-1):
    lowercase = list(string.ascii_lowercase)  # generate a list of lowercase characters in ascii
    uppercase = list(string.ascii_uppercase)  # generate a list of uppercase characters in ascii
    numbers = list(number for number in range(10))  # generate a list of numbers
    characters = list(c for c in (chr(i) for i in range(33, 48)))  # generate a list of the characters of ascii
    print("Welcome to the Password Generator\n")
    if num_lowercase <= -1 and num_uppercase <= -1 and num_characters <= -1 and num_numbers <= -1:
        # if no input is passed, ask for the user requirements for the password
        num_lowercase = int(input("How many lowercase letters would you like in your password?\n"))
        num_uppercase = int(input("How many uppercase letters would you like in your password?\n"))
        num_numbers = int(input("How many numbers would you like in your password?\n"))
        num_characters = int(input("How many characters would you like in your password?\n"))
    temp_password = ""  # to store the generated characters, letters and numbers string in the order of their generation
    password = ""  # to store the generated characters, letters and numbers string in a random order
    # generate the required number of lowercase,uppercase, numbers and characters
    # and store them in temp_password string
    for _ in range(num_lowercase):
        temp_password += choice(lowercase)
    for _ in range(num_uppercase):
        temp_password += choice(uppercase)
    for _ in range(num_characters):
        temp_password += choice(characters)
    for _ in range(num_numbers):
        temp_password += str(choice(numbers))
    temp_password = list(temp_password)  # convert the temp_password  string to  a list
    shuffle(temp_password)  # shuffle the list
    password = password.join(temp_password)  # convert the shuffled list to a password string
    print(password)
    return password


if __name__ == '__main__':
    # password_generator()
    password_generator(num_lowercase = 5, num_numbers = 5, num_characters = 5, num_uppercase = 5)
