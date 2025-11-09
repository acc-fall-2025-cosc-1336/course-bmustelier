from lists import get_lowest_list_value, get_highest_list_value


def main():
	while True:
		print("\n1-Show the list low /high values")
		print("2-Exit\n")
		choice = input("Select an option: ")

		if choice == '1':
			values = []
			while True:
				val = input("Enter a list value\n")
				try:
					num = int(val)
				except ValueError:
					print("Please enter a valid integer.")
					continue
				values.append(num)

				if len(values) >= 3:
					more = input("Do you want to enter another value? (y/n)\n")
					if more.lower().startswith('n'):
						break

			try:
				low = get_lowest_list_value(values)
				high = get_highest_list_value(values)
			except ValueError:
				print("No values were entered.")
			else:
				print(f"Lowest value: {low}")
				print(f"Highest value: {high}")

		elif choice == '2':
			break
		else:
			print("Invalid option. Please choose 1 or 2.")


if __name__ == "__main__":
	main()