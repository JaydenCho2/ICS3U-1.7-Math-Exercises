"""
File: hours.py
Author: Jayden Cho
Date: 2024-02-22 
Description: calculating how many days and hours are in given hours
"""

#Inputs of hours
hours= (float(input("Enter Duration in Hours: ")))

#Calculation days and leftover hours
days= int(hours / 24)
remain_hour= round(hours - (days * 24))

#Printing the result
print("Result: " + str(hours) + " hours is equal to " + str(days) + " days, " + str(remain_hour) + " hours")
