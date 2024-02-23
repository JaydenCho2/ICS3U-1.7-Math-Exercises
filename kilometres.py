"""
File: kilometres.py
Author: Jayden Cho
Date: 2024-02-22 
Description: Converting mile into kilometer
"""
#inputs of mile
Miles= float(input("Enter Distance in Miles: "))

#Converting mile to kilometer and rounding
kilometer= (1.609 * Miles)
rounded_kilometer= round(kilometer,2)

#printing the result
print("Result: " + str(Miles) + " miles equals " + str(rounded_kilometer) + " km")
