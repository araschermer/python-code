def reverse_integer(x):
    """Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside
     the signed 32-bit integer range [-2^31, (2^31) - 1], then return 0.
    :type x: int
    :rtype: int
    """
    x_string = str(x)
    if x_string[0] == "-":  # in case the number is negative
        x_string = x_string[1:]  # remove the negative sign
        x_string = x_string[::-1]  # reverse the number
        x_string = "-" + x_string  # append the negative sign to the new number
    else:
        x_string = x_string[::-1] # if number is positive, reverse the number
    if (-2) ** 31 <= int(x_string) < ((2 ** 31) - 1): # test boundaries of 32-bit integers
        return int(x_string) # if number is  valid, return it
    else:
        return 0 # otherwise return 0


if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-123))
    print(reverse_integer(120))
    print(reverse_integer(0))

    # Example
    # 1:
    # Input: x = 123
    # Output: 321
    # Example

    # 2:
    # Input: x = -123
    # Output: -321
    # Example

    # 3:
    # Input: x = 120
    # Output: 21
    # Example

    # 4:
    # Input: x = 0
    # Output: 0