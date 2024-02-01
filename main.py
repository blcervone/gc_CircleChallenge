# import circle_class
# Create a while loop to test for valid input
    # try:
        # get user input as a double
        # set valid input flag to terminate loop
    # except:
        # print an error
# Create and instance of the Circle class with the user input as the radius parameter
# Call and print get_diameter() on the instance created
# Call and print get_circumference() on the instance created
# Call and print get_area() on the instance created
# Create a while loop to continue asking user to grow the circle using a flag variable
    # Ask user if circle should grow (y/n)
        # If 'y':
            # Call grow() method on the instance created
            # Re-call and print:
                # get_diameter()
                # get_circumfrence()
                # get_area()
        # If 'n':
            # Print Goodbye!
            # terminate while loop by setting the flag variable

# ==================================================================================================================== #

from circle_class import *


def print_info(circle):
    print(f"Diameter: {circle.calculate_diameter()}")
    print(f"Circumference: {circle.calculate_circumference()}")
    print(f"Area: {circle.calculate_area()}")


valid_input = False
while not valid_input:
    try:
        radius_dbl = float(input("Please enter a radius value (decimals are accepted): >"))
        valid_input = True
    except:
        print("Please enter a valid number value!")

circle1 = Circle(radius_dbl)
print_info(circle1)

grow_circle = True
while grow_circle:
    ask_grow = input("Would you like your circle to grow? (y/n) >")
    if ask_grow == 'y':
        print("Standby while your circle magically grows...")
        circle1.grow()
        print_info(circle1)
    elif ask_grow == 'n':
        print(f"Goodbye!\nFinal radius value: {circle1.get_radius()}")
        grow_circle = False
    else:
        print("Invalid response!")