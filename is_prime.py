# a prime number is ony divisible by itself and the unit
# one is not prime, since it is the unit
# the basic implementation pf such a method would look like:
from nose.tools import assert_false, assert_true
from time import time
from math import sqrt, ceil


def is_prime_v1(n):
    "Return True if n is prime, otherwise False."
    if n == 1:
        return False
    elif n == 2:
        return True
    for number in range(3, n):
        if n % number == 0:
            return False
    return True


assert_true(is_prime_v1(2))
assert_true(is_prime_v1(3))
assert_true(is_prime_v1(5))
assert_true(is_prime_v1(7))
assert_false(is_prime_v1(9))
assert_false(is_prime_v1(12))
assert_false(is_prime_v1(18))


# Performance evaluation:
# start = time()
# for number in range(10000):
#     is_prime_v1(number)
# end = time()
# runtime = end - start
# print(f"The required time for is_prime_v1 is {runtime}")
# The required time is 0.5043008327484131

# Version 2: eliminate
# test only the numbers up to the square root of the given number
# for example: for a composite number 20:
# the divisors are: 1x20, 2x10, 4x5, sqrt(20):4.47, 5x4,10x2,20x1:
# so the same numbers appear twice, once before the  square root of the given number, and once after
# Therefore, one can only regard the first appearance, i.e all the numbers before the square root of the given number
# also once the number if not 2 (the only even prime number), the for loop will stop and return false, so it is wise to
# regard only the odd numbers if the given number is also odd
def is_prime_v2(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        sqrt_n = ceil(sqrt(n))+1
        for number in range(3, sqrt_n, 2):
            if n % number == 0:
                return False
        return True


assert_true(is_prime_v1(2))
assert_true(is_prime_v1(3))
assert_true(is_prime_v1(5))
assert_true(is_prime_v1(7))
assert_false(is_prime_v1(9))
assert_false(is_prime_v1(12))
assert_false(is_prime_v1(18))
assert_false(is_prime_v2(100))
assert_false(is_prime_v2(9999))
# Performance evaluation:
start = time()
# prime_numbers = ()
for number in range(10000):
    is_prime_v2(number)
    # if is_prime_v2(number):
    #     prime_numbers = prime_numbers + (number,)
end = time()
# print(prime_numbers)
runtime = end - start
print(f"The required time for is_prime_v2 is {runtime}")
# The required time for is_prime_v2 is 0.006979703903198242
