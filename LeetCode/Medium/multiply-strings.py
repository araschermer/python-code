def multiply_strings(num1, num2):
    """Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2,
    also represented as a string. Note: You must not use any built-in BigInteger library or convert the inputs to
    integer directly. :type num1: str :type num2: str :rtype: str
    """
    # correct solution, but does use  direct conversion from strings to integers
    # return str(int(num1) * int(num2))
    # another approach:
    numbers = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    int_num1 = 0
    int_num2 = 0
    for digit in num1:
        int_num1 = int_num1 * 10 + numbers[digit]  # for 123: first iter= 1*0+1=1, second=: 1*10+2=12, third=12*10+3=123
    for digit in num2:
        int_num2 = int_num2 * 10 + numbers[digit]
    print(str(int_num1*int_num2))
    return str(int_num1 * int_num2)


multiply_strings("2", "3") # 6
multiply_strings("123", "456") # 56088
multiply_strings("189", "234") # 44226
