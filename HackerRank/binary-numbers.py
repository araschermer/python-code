from nose.tools import assert_equal


def max_ones(n):
    """ Given a base-10 integer,n , convert it to binary (base-2).
    Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation.
    When working with different bases, it is common to show the base as a subscript."""
    print(bin(n))
    result = 0
    maximum = 0
    while n > 0:
        if n % 2 == 1:
            result += 1
            if result > maximum:
                maximum = result
        else:
            result = 0
        n = n // 2
    print(maximum)
    return maximum


if __name__ == '__main__':
    assert_equal(max_ones(125), 5)
    assert_equal(max_ones(10), 1)
    assert_equal(max_ones(3), 2)
    assert_equal(max_ones(13), 2)
    max_ones(-2)
