import time


#
#
def delay_decorator(function):
    def wrapper_function():
        # add something before the function
        time.sleep(5)
        function()  # also can just modify the function
        function()  # such as running the function twice
        # add something after the function

    return wrapper_function


#
#
@delay_decorator
def say_hello():
    print("Hello!")


#
def say_greetings():
    print("Greetings!")


#
# print hello after 5 seconds delay
say_hello()


delay_decorator(say_greetings)  # does not work this way

# an alternative to using @decorator_name is to call the outer_function and pass the function name and save te
# function call in a variable. then call the inner_function.
inner_wrapper_function = delay_decorator(say_greetings)  # without parentheses
inner_wrapper_function()
#
#  calculating the runtime of functions
current_time = time.time()
print(current_time)


def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        # function.__name__ is added to print the function's name out, not just the instance
        print(f"{function.__name__} run speed: {end_time - start_time}s")

    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()
