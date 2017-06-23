# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 08:36:49 2017

@author: N4th4lie

Function update_month2:    
    - 3 arguments:
        balance: the outstanding balance on the credit card
        annualInterestRate: annual interest rate as a decimal
        monthlyFixedRate: amount paid each month     
    - The function returns the balance after one month.
 
credit_card_debt_off.py:
 calculates the lowest fixed monthly payment needed
 in order pay off a credit card balance within 12 months.
 The monthly payment must be a multiple of $10. 
   
"""

def update_month2(balance,annualInterestRate,monthlyFixedPayment):
    unpaid_balance = balance - monthlyFixedPayment
    monthly_interest = annualInterestRate/12.0    
    return unpaid_balance*(1+monthly_interest)

balance = float(input("balance = "))    
annualInterestRate = float(input("annualInterestRate = "))

monthlyFixedPayment = 0
balance_init=balance
while balance > 0:
    monthlyFixedPayment += 10
    balance=balance_init
    for i in range(12):
        balance=update_month2(balance,annualInterestRate,monthlyFixedPayment)
    
print("Lowest Payment: "+str(monthlyFixedPayment))