def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# Functions are first-class objects, can be passed around as arguments.

def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)


result = calculate(add, 2, 3)
print(result)
result = calculate(multiply, 2, 3)
print(result)


# functions can be nested in other functions

def outer_function():
    print("Outer Function")

    def nested_function():
        print("Inner Function")

    return nested_function  # nested function is not activated here...


# to activate nested function
inner_function = outer_function()
inner_function()  # now the inner_function/nested_function is activated
