import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from src.homework.i_dictionaries_sets.dictionary import add_inventory, remove_inventory_widget


def main():
	widgets = {}
	while True:
		print("\nInventory Menu")
		print("1-Add or Update Item")
		print("2-Delete Item")
		print("3-Exit\n")
		choice = input("Select an option: ")

		if choice == '1':
			name = input("Enter item name: ").strip()
			if not name:
				print("Invalid name")
				continue
			qty_str = input("Enter quantity (integer, can be negative): ").strip()
			try:
				qty = int(qty_str)
			except ValueError:
				print("Quantity must be an integer")
				continue
			add_inventory(widgets, name, qty)
			print(f"Updated inventory: {name} = {widgets.get(name)}")

		elif choice == '2':
			name = input("Enter item name to delete: ").strip()
			if not name:
				print("Invalid name")
				continue
			res = remove_inventory_widget(widgets, name)
			print(res)

		elif choice == '3':
			break
		else:
			print("Invalid option. Please choose 1, 2 or 3.")


if __name__ == '__main__':
	main()