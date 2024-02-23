"""
File: kilometres.py
Author: Jayden Cho
Date: 2024-02-22 
Description: Converting mile into kilometer
"""

Miles=float(input("Enter Distance in Miles: "))
kilometer= (1.609 * Miles)
rounded_kilometer=round(kilometer,2)
print("Result: " + str(Miles) + " miles equals " + str(rounded_kilometer) + " km")
