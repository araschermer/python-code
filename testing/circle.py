from math import pi


def circle_area(r):
    if r == None:
        raise TypeError("r cannot be None")
    if type(r) == list or type is dict or type(r) is tuple:
        raise TypeError("an iterator input is not valid")
    if type(r) is complex or type(r) is str:
        raise ValueError("The radius can only be an int or a float")
    if r < 0:
        raise ValueError("The radius cannot be negative")
    return pi * (r ** 2)
