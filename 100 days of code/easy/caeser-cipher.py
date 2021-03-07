import string

alphabet = list(string.ascii_letters)
print(alphabet)


def encrypt(plain_text, shift_amount):
    encrypted_text = ""
    for letter in plain_text:
        index = 0
        index = alphabet.index(letter)
        index += shift_amount
        while index >= len(alphabet) - 1:
            index = index % 25 - 1  # to start from index 0
        encrypted_text += alphabet[index]
    print(f"the encoded text is {encrypted_text}")


def decrypt(plain_text, shift_amount):
    text = ""
    for letter in plain_text:
        index = alphabet.index(letter)
        index -= shift_amount
        while index < 0:
            index += 25
        text += alphabet[index]
    print(f"The decoded text is {text}")


# alternative solution
def ceasar(plain_text, shift_amount, direction):
    text = ""
    for letter in plain_text:
        if letter in alphabet:
            index = alphabet.index(letter)
            if letter in alphabet:
                if direction == "encode" or int(direction) == 1:
                    index += shift_amount

                    while index >= len(alphabet) - 1:
                        index = index % 25 - 1  # to start from index 0

                if direction == "decode" or int(direction) == 2:
                    index -= shift_amount
                    while index < 0:
                        index += 25  # to start counting from z if the shifting is by a value> 25
                text += alphabet[index]
        else:
            text += letter
    if direction not in ['encode', 'decode'] or int(direction) in [1, 2]:
        if int(direction) == 1:
            print(f"the encoded text is {text}")
        else:
            print(f"the decoded text is {text}")
    else:
        print(f"the {direction}d text is {text}")


def get_message_details(direction=1):
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceasar(text, shift, direction)


if __name__ == "__main__":
    encrypt("hello",3)
    decrypt("khoor",3)
    again = True
    while again:
        direction = input("Type 'encode', or 1 to encrypt. Type 'decode' or 2 to decrypt:\n").lower()
        if direction not in ['encode', 'decode', '1', '2']:
            continue
        else:
            get_message_details()

        rerun = input("another run?  type yes to continue, or no to exit\n").lower()
        if rerun!="yes":
            again = not again
            print("Goodbye")
        else: continue

