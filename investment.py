"""
File: investment.py
Author: Jayden Cho
Date: 2024-02-22 
Description: calculating futer value using given principan amount, annual interest, and number of years
"""

principal_amount=float(input("Enter Principal Amount: "))
annual_interest=float(input("Enter Annual Interest Rate: "))
years=int(input("Enter Numer of Years: "))

future_value= (principal_amount * ((1 + annual_interest) ** years))
rounded_future_value= round(future_value, 2)
print("Result: Future Value of investment is " + str(rounded_future_value))