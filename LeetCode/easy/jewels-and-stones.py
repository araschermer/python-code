# Runtime: 32 ms, faster than 63.11% of Python3 online submissions for Jewels and Stones.
# Memory Usage: 14 MB, less than 98.69% of Python3 online submissions for Jewels and Stones.
def num_jewels_in_stones(jewels: str, stones: str) -> int:
    """You're given strings jewels representing the types of stones that are jewels, and stones representing the
        stones you have. Each character in stones is a type of stone you have. You want to know how many of the
        stones you have are also jewels. Letters are case sensitive, so "a" is considered a different type of stone
        from "A". """
    num_jewels = 0
    for stone in stones:
        if stone in jewels:
            num_jewels += 1

    return num_jewels


def num_jewels_in_stones2(jewels: str, stones: str) -> int:
    """You're given strings jewels representing the types of stones that are jewels, and stones representing the
    stones you have. Each character in stones is a type of stone you have. You want to know how many of the
    stones you have are also jewels. Letters are case sensitive, so "a" is considered a different type of stone
    from "A". """
    # Runtime: 24 ms, faster than 95.74% of Python3 online submissions for Jewels and Stones.
    # Memory Usage: 14.3 MB, less than 48.17% of Python3 online submissions for Jewels and Stones.
    return sum([stones.count(jewel) for jewel in jewels])


# Example 1:
# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3
assert num_jewels_in_stones("aA", "aAAbbbb") == 3
assert num_jewels_in_stones2("aA", "aAAbbbb") == 3
# Example 2:
# Input: jewels = "z", stones = "ZZ"
# Output: 0
assert num_jewels_in_stones("z", "ZZ") == 0
assert num_jewels_in_stones2("z", "ZZ")==0
