"""
Take everything that you've learned so far and build a mortgage calculator
that determines the monthly payment assuming that interest is compounded monthly.

m = p * (j / (1 - (1 + j) ** (-n)))
m = monthly payment
p = loan amount
j = monthly interest rate
n = loan duration in months

output monthly payment
breakdown of interest and principle
"""
def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

def mortgage_calculator(loan_amount : float, monthly_interest_rate : float, loan_duration_months : float):
    # m = p * (j / (1 - (1 + j) ** (-n)))
    monthly_payment = loan_amount * (monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-loan_duration_months))) 
    return monthly_payment

if __name__ == '__main__':
    prompt("Welcome to Mortgage Calculator! You'll need to specify 1) your loan amount 2) your interest rate (as a decimal) and 3) loan duration in months")
    
    prompt("Your loan amount:")
    loan_amount = float(input())
    while invalid_number(loan_amount):
        prompt("That is an invalid number")
        loan_amount = float(input())

    prompt("Your monthly interest rate:")
    monthly_interest_rate = float(input())
    while invalid_number(monthly_interest_rate):
        prompt("That is an invalid number")
        monthly_interest_rate = float(input())


    prompt("Your loan duration in months:")
    loan_duration_months = float(input())
    while invalid_number(loan_duration_months):
        prompt("That is an invalid number")
        loan_duration_months = float(input())  
    
    monthly_payment = mortgage_calculator(loan_amount, monthly_interest_rate, loan_duration_months)
    print(f"Your monthly payment will be ${monthly_payment}")

