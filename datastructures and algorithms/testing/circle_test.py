from unittest import TestCase
from circle import circle_area
from math import pi


class TestCircleArea(TestCase):
    def test_circle_area(self):
        # test area when radius >= 0
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(3), pi * (3 ** 2))

    def test_values(self):
        # Make sure value errors are raised when the radius value is invalid
        self.assertRaises(ValueError, circle_area, -1)
        self.assertRaises(ValueError, circle_area, 2j + 0)
        self.assertRaises(ValueError, circle_area, "s")

    def test_types(self):
        self.assertRaises(TypeError, circle_area, None)
        self.assertRaises(TypeError, circle_area, [1, 2])
        self.assertRaises(TypeError, circle_area, {4})
        self.assertRaises(TypeError, circle_area, (8,))


if __name__ == '__main__':
    test = TestCircleArea()
    test.test_circle_area()
