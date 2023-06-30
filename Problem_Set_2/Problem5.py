# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 16:12:23 2023

@author: Cristian David Polo Garrido
"""

def lowest_payment(annualInterestRate, balance):
    Monthly_interest_rate = annualInterestRate/12.0
    fixed_monthly_payment = 10

    while (fixed_monthly_payment < balance):
        monthly_unpaid_balance = 0
        interest = 0
        remaining_balance = balance

        for month in range(1, 13):
            monthly_unpaid_balance = remaining_balance - fixed_monthly_payment
            interest = Monthly_interest_rate * monthly_unpaid_balance
            remaining_balance = monthly_unpaid_balance + interest
        if remaining_balance <= 0:
            break
        fixed_monthly_payment += 10

    print('Lowest Payment:', fixed_monthly_payment)