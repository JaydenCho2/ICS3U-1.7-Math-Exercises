"""
File: rads.py
Author: Jayden Cho
Date: 2024-02-22 
Description: Calculating radians using given degrees
"""
#input of degrees and value of pi
Degrees= int(input("Enter Degrees: "))
pi= 3.14159

#Calculating radians and rounding
radians= (Degrees * (pi / 180))
rounded_radians= round(radians, 4)

#printing the result
print("Result: " + str(Degrees) + " degrees is " + str(rounded_radians) + " radians")