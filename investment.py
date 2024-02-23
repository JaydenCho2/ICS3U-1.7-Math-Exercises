"""
File: investment.py
Author: Jayden Cho
Date: 2024-02-22 
Description: calculating futer value using given principan amount, annual interest, and number of years
"""
#Inputs of needed values
principal_amount= float(input("Enter Principal Amount: "))
annual_interest= float(input("Enter Annual Interest Rate: "))
years= int(input("Enter Numer of Years: "))

#Calculating and rounding
future_value= (principal_amount * ((1 + annual_interest) ** years))
rounded_future_value= round(future_value, 2)

#Printing the result
print("Result: Future Value of investment is " + str(rounded_future_value))