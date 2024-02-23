"""
File: exponent.py
Author: Jayden Cho
Date: 2024-02-22 
Description: creating and calculating exponent using given base and power
"""
#Inputs of base and power
Base= float(input("Enter Base: "))
Power= float(input("Enter Power: "))

#Calculation and rounding
exponent= (Base ** Power)
rounded_exponent= round(exponent, 2)

#print the result
print("Result: a^b is " + str(rounded_exponent))