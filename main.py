import math

print("Welcome to Coordinate Distance Calculator")

X1 = input("Enter Coordinates of X1(eg. 3 ) : ")
Y1 = input("Enter Coordinates of Y1(eg. 6 ) : ")
X2 = input("Enter Coordinates of X2(eg. 9 ) : ")
Y2 = input("Enter Coordinates of Y2(eg. 2 ) : ")


Distance  = math.sqrt( (int(X2)-int(X1))**2 + (int(Y2)-int(Y1))**2 )

print(f"Distance between points ({X1},{Y1}) and ({X2},{Y2}) is: " + str(Distance))

# A program to calculate distance between two points.
# Just made a basic program when I encountered my class 10 problem. Ch-7 Coordinate Geometry
# Author : Dev Shah 
# Date : 29/8/2021
