from math import pi


def circle_area(radius):
    if radius is None:
        raise TypeError("radius cannot be None")
    if type(radius) == list or type is dict or type(radius) is tuple:
        raise TypeError("an iterator input is not valid")
    if type(radius) is complex or type(radius) is str:
        raise ValueError("The radius can only be an int or a float")
    if radius < 0:
        raise ValueError("The radius cannot be negative")
    return pi * (radius ** 2)
