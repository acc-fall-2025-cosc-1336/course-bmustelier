from repetition import get_factorial, sum_odd_numbers

def main():
    while True:
        print("\nHomework 4 Menu")
        print("1-Factorial")
        print("2-Sum odd numbers")
        print("3-Exit\n")
        choice = input("Select an option: ")

        if choice == '1':
            while True:
                num_str = input("Enter a number (1-9): ")
                try:
                    num = int(num_str)
                except ValueError:
                    print("Invalid input. Please enter an integer.")
                    continue
                if 1 <= num < 10:
                    print(f"Factorial of {num} is {get_factorial(num)}")
                    break
                else:
                    print("Number must be between 1 and 9.")
        elif choice == '2':
            while True:
                num_str = input("Enter a number (1-99): ")
                try:
                    num = int(num_str)
                except ValueError:
                    print("Invalid input. Please enter an integer.")
                    continue
                if 1 <= num < 100:
                    print(f"Sum of odd numbers up to {num} is {sum_odd_numbers(num)}")
                    break
                else:
                    print("Number must be between 1 and 99.")
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
