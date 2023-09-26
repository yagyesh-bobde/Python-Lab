# AIM: Write a program that calculates the distance between two points P1(x1, y1) and P2(x2, y2).

import math

print("Enter coordinates for Point 1... ")
x1 = int(input("Enter x1 coordinate: "))
y1 = int(input("Enter y1 coordinate: "))

print("Enter coordinates for Point 2... ")
x2 = int(input("Enter x2 coordinate: "))
y2 = int(input("Enter y2 coordinate: "))

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Calculating Distance....")

print("\nThe distance bemtween the two points is: ", distance)