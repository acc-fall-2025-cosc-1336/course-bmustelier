def get_sales_tax_amount(meal_amount):
    tax_rate = 0.0675
    return meal_amount * tax_rate

def get_tip_amount(meal_amount, tip_rate):
    return meal_amount * tip_rate