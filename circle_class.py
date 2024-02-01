# import math
# Define the Circle class
    # Define __init__ function with self and radius as an instance variable
    # Define the class methods
        # Define calculate_diameter()
            # diameter = 2 * radius
        # Define calculate_circumference()
            # circumference = 2 * pi * radius
        # Define calculate_area()
            # area = pi * radius**2
        # Define grow()
            # self.radius = self.radius * 2
        # Define get_radius()
            # print(self.radius)

# ==================================================================================================================== #

import math


class Circle:

    def __init__(self, init_radius):
        self.radius = init_radius

    def calculate_diameter(self):
        return self.radius * 2

    def calculate_circumference(self):
        return 2 * math.pi * self.radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def grow(self):
        self.radius = self.radius * 2

    def get_radius(self):
        return self.radius
