# Create a function named calculate_area that computes the area of a rectangle. 
# The function should accept two parameters: length and width. 
# Demonstrate its usage by calculating the area for a rectangle with a length of 5 units and a width of 3 units.
import math
def calculate_area(lenght,breadth):
    area = lenght * breadth
    return area
lenght= float(input("Enter the lenght of the rectangle: "))
breadth= float(input("Enter the breadth of the rectangle: "))
print("The area of the rectangle is: ", calculate_area(lenght,breadth))

calculate_area(lenght ,breadth)


