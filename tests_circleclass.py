import unittest
from circle_class import *

c1 = Circle(5)

class Validator(unittest.TestCase):
    def test_diameter1(self):
        self.assertEqual(Circle(5).calculate_diameter(), 10.0)  # Circle with radius 5 should return diameter 10

    def test_diameter2(self):
        self.assertEqual(Circle(2.5).calculate_diameter(), 5.0)  # Circle with radius 2.5 should return diameter 5

    def test_circumference(self):
        self.assertEqual(Circle(5).calculate_circumference(), 31.41592653589793)

    def test_circumference2(self):
        self.assertEqual(Circle(10).calculate_circumference(), 62.83185307179586)

    def test_area(self):
        self.assertEqual(Circle(10).calculate_area(), 314.1592653589793)


if __name__ == '__main__':
    unittest.main()
