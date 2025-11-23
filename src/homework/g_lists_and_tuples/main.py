import os
import sys

# Ensure repo root is on sys.path so `import src...` works when run as a script
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from src.homework.g_lists_and_tuples.lists import get_p_distance_matrix


def prompt_sequences():
	while True:
		try:
			n = int(input("How many sequences? (1-10): "))
		except ValueError:
			print("Please enter a valid integer.")
			continue
		if n < 1 or n > 10:
			print("Please enter a number between 1 and 10.")
			continue
		break

	seqs = []
	length = None
	for i in range(1, n + 1):
		while True:
			s = input(f"Enter sequence #{i} (letters only, no spaces): ").strip().upper()
			if not s:
				print("Sequence cannot be empty.")
				continue
			# convert to list of characters
			chars = list(s)
			if length is None:
				length = len(chars)
			if len(chars) != length:
				print(f"All sequences must have the same length ({length}). Try again.")
				continue
			seqs.append(chars)
			break

	return seqs


def main():
	while True:
		print("\n1-Get p distance matrix")
		print("2-Exit\n")
		choice = input("Select an option: ")

		if choice == '1':
			seqs = prompt_sequences()
			try:
				matrix = get_p_distance_matrix(seqs)
			except Exception as e:
				print(f"Error computing matrix: {e}")
				continue
			for row in matrix:
				print(' '.join(f"{x:.5f}" for x in row))

		elif choice == '2':
			break
		else:
			print("Invalid option. Please choose 1 or 2.")


if __name__ == '__main__':
	main()