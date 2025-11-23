def get_p_distance(list1, list2):
	if len(list1) != len(list2):
		raise ValueError("Lists must have the same length")
	if len(list1) == 0:
		return 0.0
	diffs = 0
	for a, b in zip(list1, list2):
		if a != b:
			diffs += 1
	return diffs / float(len(list1))


def get_p_distance_matrix(list1):
	n = len(list1)
	p_distance_matrix = [[0.0 for _ in range(n)] for _ in range(n)]
	for i in range(n):
		for j in range(i, n):
			d = get_p_distance(list1[i], list1[j])
			p_distance_matrix[i][j] = d
			p_distance_matrix[j][i] = d
	return p_distance_matrix