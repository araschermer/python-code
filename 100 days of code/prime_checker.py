def is_prime(number):
    """checks if a given number is prime"""
    prime = True
    for n in range(2, number):
        if prime and number % n == 0:
            prime = False
            print("The number is not prime")
    if prime:
        print("The number is prime")
    return prime


if __name__ == "__main__":
    is_prime(19)
    is_prime(23)
    is_prime(89)
    is_prime(97)
    is_prime(55)
