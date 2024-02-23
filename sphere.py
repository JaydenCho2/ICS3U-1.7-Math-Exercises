"""
File: sphere.py
Author: Jayden Cho
Date: 2024-02-22 
Description: Calculating volume using given radius
"""

Radius=float(input("Enter Radius: "))
pi=3.14159

Volume=((4 / 3) * (pi * (Radius**3)))
rounded_volume= round(Volume, 2)

print("Result: Volume is " + str(rounded_volume))