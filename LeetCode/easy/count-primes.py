def count_primes(n):
    """Count the number of prime numbers less than a non-negative number, n.
    # extra: return the prime numbers
    :type n: int
    :rtype: int
    """
    prime_numbers = []
    if n < 2:
        return 0
    prime = [1] * n  # fill a list of length n with 1
    for i in range(2, n):
        if prime[i]:
            prime[i * i:n:i] = [0] * len(prime[i * i:n:i])  # set all multiples of i to 0
    for i, value in enumerate(prime):  # to print the prime numbers themselves
        if value == 1 and i >= 2:  # only consider values= 1, since those are the prime numbers, disregard 1 and 0
            prime_numbers.append(i)  # append the (prime)number to the prime numbers list
    print(prime_numbers)
    return sum(prime[2:])


if __name__ == '__main__':
    # Example 1:
    # Input: n = 10
    # Output: 4
    # Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
    print(count_primes(10))
    # Example 2:
    # Input: n = 0
    # Output: 0
    print(count_primes(0))
    # Example 3:
    # Input: n = 1
    # Output: 0
    print(count_primes(1))