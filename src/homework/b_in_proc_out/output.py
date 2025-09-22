def get_sales_tax_amount(meal_amount):
    """
    Calculate the sales tax amount for a given meal amount.

    Parameters:
        meal_amount (float): The cost of the meal.

    Returns:
        float: The calculated sales tax amount.
    """
    tax_rate = 0.0675
    return meal_amount * tax_rate
    return meal_amount * TAX_RATE

def get_tip_amount(meal_amount, tip_rate):
    return meal_amount * tip_rate