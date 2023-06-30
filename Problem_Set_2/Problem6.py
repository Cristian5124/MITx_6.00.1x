# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 15:31:54 2023

@author: Cristian David Polo Garrido
"""

def lowest_exact_payment(annualInterestRate, balance):    
    monthlyInterestRate = annualInterestRate / 12.0

    monthly_lower_bound = balance / 12
    monthly_upper_bound = (balance * ((1 + monthlyInterestRate)** 12)) /12.0

    remaining_balance = balance

    while (remaining_balance != 0):
        fixed_monthly_payment = (monthly_lower_bound + monthly_upper_bound)/2
        monthly_unpaid_balance = 0
        interest = 0
        remaining_balance = balance

        for month in range (1, 13):
            monthly_unpaid_balance = remaining_balance - fixed_monthly_payment
            interest = monthlyInterestRate * monthly_unpaid_balance
            remaining_balance = monthly_unpaid_balance + interest

        if remaining_balance <= 0:
            monthly_upper_bound = fixed_monthly_payment

        elif remaining_balance >= 0:
            monthly_lower_bound = fixed_monthly_payment

        remaining_balance = round (remaining_balance, 2)
    print('Lowest Payment:', round (fixed_monthly_payment, 2))