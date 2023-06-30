# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 10:44:39 2023

@author: Cristian David Polo Garrido
"""

def rem_balance(annualInterestRate, monthlyPaymentRate):
    cont=0
    while cont<12:
        Monthly_interest_rate = annualInterestRate/12.0
        Minimum_monthly_payment = monthlyPaymentRate * balance
        Monthly_unpaid_balance = balance - Minimum_monthly_payment
        balance = Monthly_unpaid_balance + (Monthly_interest_rate * Monthly_unpaid_balance)
        cont+=1
    print('Remaining balance: '+str(round(balance,2)))