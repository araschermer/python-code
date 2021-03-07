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

    # if direction=="encode":
    encrypt(plain_text = text, shift_amount = shift)
    # elif direction=="decode":
    decrypt(plain_text = text, shift_amount = shift)
    # else:
    print("Wrong input ")


# alternative solution
def ceasar(plain_text, shift_amount, direction):
    text = ""
    for letter in plain_text:
        if letter in alphabet:
            index = alphabet.index(letter)
            if letter in alphabet:
                if direction == "encode" or direction == 1:
                    index += shift_amount

                    while index >= len(alphabet) - 1:
                        index = index % 25 - 1  # to start from index 0

                if direction == "decode" or direction == 2:
                    index -= shift_amount
                    while index < 0:
                        index += 25  # to start counting from z if the shifting is by a value> 25
                text += alphabet[index]
        else:
            text += letter

    print(f"the {direction}d text is {text}")


if __name__ == "__main__":
    again = True
    while again:
        direction = input("Type 'encode'  or 1 to encrypt, type 'decode' or 2 to decrypt:\n").lower()
        if direction not in ['encode', 'decode', 1, 2]:
            continue
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        ceasar(text, shift, direction)
        rerun = input("another run?  type yes to continue, or no to exit\n").lower()
        if rerun == "no":
            again = not again
            print("Goodbye")
