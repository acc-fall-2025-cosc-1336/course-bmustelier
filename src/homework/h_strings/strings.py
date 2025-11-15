
def get_hamming_distance(dna1, dna2):
	count1 = 0
	for _ in dna1:
		count1 += 1

	count2 = 0
	for _ in dna2:
		count2 += 1

	if count1 != count2:
		raise ValueError("dna1 and dna2 must be of equal length")

	distance = 0
	i = 0
	while i < count1:
		if dna1[i] != dna2[i]:
			distance += 1
		i += 1
	return distance



def get_dna_complement(dna):
	length = 0
	for _ in dna:
		length += 1

	i = length - 1
	result = ''
	while i >= 0:
		base = dna[i]
		if base == 'A':
			comp = 'T'
		elif base == 'T':
			comp = 'A'
		elif base == 'C':
			comp = 'G'
		elif base == 'G':
			comp = 'C'
		else:
			comp = base
		result = result + comp
		i -= 1
	return result