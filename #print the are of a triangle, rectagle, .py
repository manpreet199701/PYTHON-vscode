#print the are of a triangle, rectagle, and circle
#ask the user to chose btwkkk the three shapes
#ask the user to enter the dimensions of the chosen shape
#display the area of the chosen shape
#def area_triangle(base, height):
#return base*height/2:
#area_a = area_triangle (5,4)
#area_b = area_triangle(7,3)
#sum = area_a + area_b
#print("The sum of both areas is: " + str(sum))
#The sum of both areas is: 20.5
import math
def are_shape():
    shape = input("Enter the shape you want to calculate the area for: ")
    if shape == "triangle":
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = 0.5 * base * height
        print("The area of the triangle is: ", area)
    elif shape == "rectangle":
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = length * width
        print("The area of the rectangle is: ", area)
    elif shape == "circle":
        radius = float(input("Enter the radius of the circle: "))
        area = math.pi * radius ** 2
        print("The area of the circle is: ", area)
    else:
        print("Invalid shape entered.")
are_shape()

      
            