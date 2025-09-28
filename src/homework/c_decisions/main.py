from decisions import get_letter_grade, get_options_ratio, get_faculty_rating

def get_letter_grade_switch(score):
    """Return the letter grade using a switch-like structure (Python 3.10+ match/case)."""
    match score:
        case s if s >= 90:
            return 'A'
        case s if s >= 80:
            return 'B'
        case s if s >= 70:
            return 'C'
        case s if s >= 60:
            return 'D'
        case _:
            return 'F'

def main():
    print("\nMAIN MENU\n")
    print("1-Letter grade using if")
    print("2-Letter grade using switch")
    print("3-Exit\n")
    option = input("Select an option: ")

    if option == '1':
        score_str = input("Enter a number between 0 and 100: ")
        try:
            score = int(score_str)
        except ValueError:
            print("Invalid input. Please enter a number.")
            return
        if 0 <= score <= 100:
            print(f"Letter grade (if): {get_letter_grade(score)}")
        else:
            print("Number is out of range.")
    elif option == '2':
        score_str = input("Enter a number between 0 and 100: ")
        try:
            score = int(score_str)
        except ValueError:
            print("Invalid input. Please enter a number.")
            return
        if 0 <= score <= 100:
            print(f"Letter grade (switch): {get_letter_grade_switch(score)}")
        else:
            print("Number is out of range.")
    elif option == '3':
        print("Exiting program.")
    else:
        print("Invalid option.")

    # Prompt for options and total, then output faculty rating
    option_str = input("Enter the number of options: ")
    total_str = input("Enter the total: ")
    try:
        option_val = float(option_str)
        total_val = float(total_str)
    except ValueError:
        print("Invalid input. Please enter numbers.")
    else:
        ratio = get_options_ratio(option_val, total_val)
        rating = get_faculty_rating(ratio)
        print(f"Faculty Rating: {rating}")

if __name__ == "__main__":
    main()