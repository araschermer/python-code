def add_all_numbers(n):
    """adds all numbers between zero and n, including n"""
    return sum([number for number in range(n + 1)])


def add_odd_numbers(n):
    """adds all odd number between zero and n, including n"""
    return sum([number for number in range(n + 1) if number % 2 != 0])
    # another approach
    # return sum([number for number in range(1,n + 1,2) ])


def add_even_numbers(n):
    """adds all even number between zero and n, including n"""
    return sum([number for number in range(n + 1) if number % 2 == 0])
    # another approach 
    # return sum([number for number in range(2,n + 1,2) ])


if __name__ == '__main__':
    print(add_all_numbers(100))
    print(add_odd_numbers(100))
    print(add_even_numbers(100))
