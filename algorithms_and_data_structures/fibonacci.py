from time import time
# Implementation using a decorator
# to store least recently used cache

from functools import lru_cache


@lru_cache(maxsize=1000)
def fibonacci_with_decorator(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_with_decorator(n - 1) + fibonacci_with_decorator(n - 2)


start = time()
(fibonacci_with_decorator(500))
end = time()
runtime = end - start
# runtime=0.0009982585906982422


#  explicit implementation of fibonacci function
# here a dict caches/stored the already calculated values of the fibonacci function
# and uses them in the next calculation that would require the fibonacci  of a stored number
fibonacci_cached = {}


def fibonacci(n):
    if n in fibonacci_cached:
        return fibonacci_cached[n]
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n - 1) + fibonacci(n - 2)
    fibonacci_cached[n] = value
    return value


fibonacci(900)
# basic implementation
num1, num2 = 0, 1
for _ in range(0, 10):
    print(num1)
    num1, num2 = num2, num1 + num2


#  implementation using generator
def fibonacci(number_):
    num1, num2 = 0, 1
    for number in range(0, number_):
        yield f"{number + 1}:{num1}"
        num1, num2 = num2, num1 + num2


for number in fibonacci(10):
    print(number)
