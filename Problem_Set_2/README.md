<h1 align="center">Problem Set 2</h1>

### Problem 1 - Paying Debt off in a Year

<hr>

Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

<br>

The following variables contain values as described below:
  1. `balance` - the outstanding balance on the credit card
  2. `annualInterestRate` - annual interest rate as a decimal
  3. `monthlyPaymentRate` - minimum monthly payment rate as a decimal

<br>

For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, print out the remaining balance. Be sure to print out no more than two decimal digits of accuracy - so print <br>

    Remaining balance: 813.41

instead of

    Remaining balance: 813.4141998135

So your program only prints out one thing: the remaining balance at the end of the year in the format:

    Remaining balance: 4784.0

<br>

A summary of the required math is found below:

  * __Monthly interest rate__ = (Annual interest rate) / 12.0  <br>
  * __Minimum monthly payment__ = (Minimum monthly payment rate) x (Previous balance)  <br>
  * __Monthly unpaid balance__ = (Previous balance) - (Minimum monthly payment)  
  * __Updated balance each month__ = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

<br>

### **Problem 1 Test Cases**

**Note**: Depending on where you round in this problem, your answers may be off by a few cents in either direction. Do not worry if your solution is within +/- 0.05 of the correct answer.

<br>

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

[Problem 1](Problem4.py)

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

### Problem 2 - Paying Debt Off in a Year

<hr>

Now write a program that calculates the minimum **fixed** monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.

<br>

In this problem, we will *not* be dealing with a minimum monthly payment rate. <br>
The following variables contain values as described below: <br>
  1. `balance` - the outstanding balance on the credit card
  2. `annualInterestRate` - annual interest rate as a decimal

<br>

The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year, for example: <br>

    Lowest Payment: 180

<br>

Assume that the interest is compounded monthly according to the balance at the end of the month (after the payment for that month is made). The monthly payment must be a multiple of $10 and is the same for all months. Notice that it is possible for the balance to become negative using this payment scheme, which is okay. A summary of the required math is found below:

  * __Monthly interest rate__ = (Annual interest rate) / 12.0
  * __Monthly unpaid balance__ = (Previous balance) - (Minimum fixed monthly payment)
  * __Updated balance each month__ = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

<br>

### **Problem 2 Test Cases**

**Test Cases**:

    # Test Case 1:
    balance = 3329
    annualInterestRate = 0.2

    Result Your Code Should Generate:
    -------------------
    Lowest Payment: 310

<br>

    # Test Case 2:
    balance = 4773
    annualInterestRate = 0.2
    
    Result Your Code Should Generate:
    -------------------
    Lowest Payment: 440

<br>

    # Test Case 3:
    balance = 3926
    annualInterestRate = 0.2

    Result Your Code Should Generate:
    -------------------
    Lowest Payment: 360
    

### Solution

<hr>

[Problem 2](Problem5.py)

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

### Problem 3 - Using Bisection Search to Make the Program Faster

<hr>

You'll notice that in Problem 2, your monthly payment had to be a multiple of $10. Why did we make it that way? You can try running your code locally so that the payment can be any dollar and cent amount (in other words, the monthly payment is a multiple of $0.01). Does your code still work? It should, but you may notice that your code runs more slowly, especially in cases with very large balances and interest rates. 

<br>

Well then, how can we calculate a more accurate fixed monthly payment than we did in Problem 2 without running into the problem of slow code? We can make this program run faster using a technique introduced in lecture - *bisection search*!

<br>

The following variables contain values as described below: <br>
  1. `balance` - the outstanding balance on the credit card
  2. `annualInterestRate` - annual interest rate as a decimal

<br>

**To recap the problem**: We are searching for the smallest monthly payment such that we can pay off the entire balance within a year. What is a reasonable lower bound for this payment value? $0 is the obvious answer, but you can do better than that. If there was no interest, the debt can be paid off by monthly payments of one-twelfth of the original balance, so we must pay at least this much every month. One-twelfth of the original balance is a good lower bound.

<br>

**What is a good upper bound?** Imagine that instead of paying monthly, we paid off the entire balance at the end of the year. What we ultimately pay must be greater than what we would've paid in monthly installments, because the interest was compounded on the balance we didn't pay off each month. So a good upper bound for the monthly payment would be one-twelfth of the balance, *after* having its interest compounded monthly for an entire year.

<br>

In short: <br>
  * __Monthly interest rate__ = (Annual interest rate) / 12.0
  * __Monthly payment lower bound__ = Balance / 12
  * __Monthly payment upper bound__ = (Balance x (1 + Monthly interest rate)^12) / 12.0

<br>

Write a program that uses these bounds and bisection search to find the smallest monthly payment to the cent (no more multiples of $10) such that we can pay off the debt within a year. Try it out with large inputs, and notice how fast it is (try the same large inputs in your solution to Problem 2 to compare!). Produce the same return value as you did in Problem 2.

<br>

### **Problem 3 Test Cases**

**Test Cases**:

    # Test Case 1:
    balance = 320000
    annualInterestRate = 0.2

    Result Your Code Should Generate:
    -------------------
    Lowest Payment: 29157.09

<br>

    # Test Case 2:
    balance = 999999
    annualInterestRate = 0.18
    
    Result Your Code Should Generate:
    -------------------
    Lowest Payment: 90325.03
    

### Solution

<hr>

[Problem 3](Problem6.py)

    # -*- coding: utf-8 -*-
    """
    Created on Thu Jun 22 17:31:54 2023
    
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
