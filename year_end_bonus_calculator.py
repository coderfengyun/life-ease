### co-created with chatgpt

def calculate_bonus_tax(annual_bonus):
    """
    Calculate the tax for an annual bonus based on the progressive tax brackets.

    :param annual_bonus: Total annual bonus amount
    :return: Total tax amount
    """
    # Define tax brackets as (upper limit, rate, quick deduction)
    tax_brackets = [
        (3000, 0.03, 0), 
        (12000, 0.10, 210),
        (25000, 0.20, 1410),
        (35000, 0.25, 2660),
        (55000, 0.30, 4410),
        (80000, 0.35, 7160),
        (float('inf'), 0.45, 15160)
    ]

    # Calculate monthly equivalent income
    monthly_income = annual_bonus / 12

    # Initialize tax calculation variables
    total_tax = 0
    previous_limit = 0

    # Loop through each bracket to calculate progressive tax
    for limit, rate, deduction in tax_brackets:
        taxable_income = min(limit, monthly_income) - previous_limit
        if taxable_income > 0:
            total_tax += taxable_income * rate
        if monthly_income <= limit:
            break
        previous_limit = limit

    # Adjust total tax with the quick deduction for the bracket
    quick_deduction = next(d for l, r, d in tax_brackets if monthly_income <= l)
    total_tax = total_tax * 12 - quick_deduction

    return total_tax

# Test the function with the provided annual bonus
annual_bonus = 493798.136
bonus_tax = calculate_bonus_tax(annual_bonus)
print(bonus_tax)
