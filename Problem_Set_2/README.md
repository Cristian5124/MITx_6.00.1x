<h1 align="center">Problem Set 2</h1>

### Problem 1 - Paying Debt off in a Year

<hr>

Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

<br>

The following variables contain values as described below:
  1. `balance` - the outstanding balance on the credit card
  2. `annualInterestRate` - annual interest rate as a decimal
  3. `monthlyPaymentRate` - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, print out the remaining balance. Be sure to print out no more than two decimal digits of accuracy - so print <br>

    Remaining balance: 813.41

instead of

    Remaining balance: 813.4141998135

So your program only prints out one thing: the remaining balance at the end of the year in the format:

    Remaining balance: 4784.0

A summary of the required math is found below:

  * __Monthly interest rate__ = (Annual interest rate) / 12.0  <br>
  * __Minimum monthly payment__ = (Minimum monthly payment rate) x (Previous balance)  <br>
  * __Monthly unpaid balance__ = (Previous balance) - (Minimum monthly payment)  
  * __Updated balance each month__ = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

<br>

### **Problem 1 Test Cases**

**Note**: Depending on where you round in this problem, your answers may be off by a few cents in either direction. Do not worry if your solution is within +/- 0.05 of the correct answer.

**Test Cases**:

    # Test Case 1:
    balance = 42
    annualInterestRate = 0.2
    monthlyPaymentRate = 0.04
    
    # Result Your Code Should Generate Below:
    Remaining balance: 31.38
                
      # To make sure you are doing calculation correctly, this is the 
      # remaining balance you should be getting at each month for this example
        Month 1 Remaining balance: 40.99
        Month 2 Remaining balance: 40.01
        Month 3 Remaining balance: 39.05
        Month 4 Remaining balance: 38.11
        Month 5 Remaining balance: 37.2
        Month 6 Remaining balance: 36.3
        Month 7 Remaining balance: 35.43
        Month 8 Remaining balance: 34.58
        Month 9 Remaining balance: 33.75
        Month 10 Remaining balance: 32.94
        Month 11 Remaining balance: 32.15
        Month 12 Remaining balance: 31.38

<br>

    # Test Case 2:
    balance = 484
    annualInterestRate = 0.2
    monthlyPaymentRate = 0.04
    
    Result Your Code Should Generate Below:
    Remaining balance: 361.61

### Solution

<hr>

[Problema 1](Problem4.py)

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