def main():
    # Get meal amount from user
    meal_str = input("Enter the meal amount (e.g., 20.50): $")
    try:
        meal_amount = float(meal_str)
    except ValueError:
        print("Invalid meal amount.")
        return

    # Get tip percentage from user
    tip_str = input("Enter tip percentage (whole number or decimal, e.g., 15 or 18.5 for 15% or 18.5%): ")
    try:
        tip_percent = float(tip_str)
    except ValueError:
        print("Invalid tip percentage.")
        return

    tax_rate = 0.0675
    tax = meal_amount * tax_rate
    tip = meal_amount * (tip_percent / 100)
    total = meal_amount + tax + tip

    print("\n--- Receipt ---")
    print("Meal Amount:   $%s" % meal_amount)
    print("Sales Tax:     $%s" % tax)
    print("Tip:           $%s" % tip)
    print("Total:         $%s" % total)

if __name__ == "__main__":
    main()