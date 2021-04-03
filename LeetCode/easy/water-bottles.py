from nose.tools import assert_equal


def num_water_bottles(num_bottles: int, num_exchange: int) -> int:
    """Given numBottles full water bottles, you can exchange numExchange empty water bottles for one full water bottle.
    The operation of drinking a full water bottle turns it into an empty bottle.
    Return the maximum number of water bottles you can drink."""
    if num_bottles < num_exchange:
        return num_bottles
    # the maximum number of water bottles without any exchanges are obviously  the given number of water bottles
    max_exchanges = num_bottles
    # if we can still exchange, then loop
    while num_bottles >= num_exchange:
        # number of  bottle to exchange are the floor of the total number of water bottles
        # divided by the exchange cost(num_exchange)
        to_exchange = num_bottles // num_exchange
        # add the number of bottle to exchange to the max number of water to drink
        max_exchanges += to_exchange
        # the number of bottle that are left out of the last exchange are
        # the number of water bottles modulo exchange cost(num_exchange)
        not_exchanged = num_bottles % num_exchange
        #  the number of bottle that are still left to exchange are the number of bottles to exchange
        #  plus the number of water bottles that are  not used in the previous exchange
        num_bottles = to_exchange + not_exchanged
    return max_exchanges


if __name__ == '__main__':
    # Input: numBottles = 9, numExchange = 3
    # Output: 13
    # Explanation: You can exchange 3 empty bottles to get 1 full water bottle.
    # Number of water bottles you can drink: 9 + 3 + 1 = 13.
    assert_equal(num_water_bottles(9, 3), 13)
    # Input: numBottles = 15, numExchange = 4
    # Output: 19
    # Explanation: You can exchange 4 empty bottles to get 1 full water bottle.
    # Number of water bottles you can drink: 15 + 3 + 1 = 19.
    assert_equal(num_water_bottles(15, 4), 19)
    # Input: numBottles = 5, numExchange = 5
    # Output: 6
    assert_equal(num_water_bottles(5, 5), 6)
    # Input: numBottles = 2, numExchange = 3
    # Output: 2
    assert_equal(num_water_bottles(2, 3), 2)
