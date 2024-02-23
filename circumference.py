"""
File: circumference.py
Author: Jayden Cho
Date: 2024-02-22 
Description: finding circumference using given radius
"""
#Inputs of radius and value of pi
radius= float(input("Enter Radius: "))
pi= 3.14159

#Calculating using given radius and pi and rounding
circumference= float(2 * (radius * pi))
rounded_circumference= round(circumference, 2)

#printing the result
print("Result: " + str(rounded_circumference))
