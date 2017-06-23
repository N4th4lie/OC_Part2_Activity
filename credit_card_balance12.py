# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 08:36:49 2017

@author: N4th4lie

Function update_month:    
    - 3 arguments:
        balance: the outstanding balance on the credit card
        annualInterestRate: annual interest rate as a decimal
        monthlyPaymentRate: minimum monthly payment rate as a decimal      
    - The function returns the balance after one month.
        
"""

def update_month(balance,annualInterestRate,monthlyPaymentRate):
    minimum_payment = monthlyPaymentRate*balance
    unpaid_balance = balance - minimum_payment
    monthly_interest = annualInterestRate/12.0    
    return unpaid_balance*(1+monthly_interest)

balance = float(input("balance = "))    
annualInterestRate = float(input("annualInterestRate = "))
monthlyPaymentRate = float(input("monthlyPaymentRate = "))

for i in range(12):
    balance=update_month(balance,annualInterestRate,monthlyPaymentRate)
    
print("Remaining balance: "+str(round(balance,2)))