from strings import get_hamming_distance, get_dna_complement


def main():
	while True:
		print("\n1-Hamming Distance")
		print("2-Dna Complement")
		print("3-Exit\n")
		choice = input("Select an option: ")

		if choice == '1':
			s1 = input("Enter first DNA string: ")
			s2 = input("Enter second DNA string: ")
			try:
				dist = get_hamming_distance(s1, s2)
			except ValueError:
				print("Error: strings must be of equal length.")
			else:
				print(f"Hamming distance: {dist}")
		elif choice == '2':
			s = input("Enter DNA string: ")
			comp = get_dna_complement(s)
			print(f"Reverse complement: {comp}")
		elif choice == '3':
			break
		else:
			print("Invalid option. Please choose 1, 2 or 3.")


if __name__ == "__main__":
	main()