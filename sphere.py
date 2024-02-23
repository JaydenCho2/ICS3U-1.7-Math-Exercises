"""
File: sphere.py
Author: Jayden Cho
Date: 2024-02-22 
Description: Calculating volume using given radius
"""
#Input of radius and value of pi
Radius= float(input("Enter Radius: "))
pi= 3.14159

#Calculating volume and rounding
Volume= ((4 / 3) * (pi * (Radius ** 3)))
rounded_volume= round(Volume, 2)

#printing result
print("Result: Volume is " + str(rounded_volume))