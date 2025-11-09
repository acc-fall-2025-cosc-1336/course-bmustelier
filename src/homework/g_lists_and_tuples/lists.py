
def get_lowest_list_value(values):
	first = True
	lowest = None
	for v in values:
		if first:
			lowest = v
			first = False
		else:
			if v < lowest:
				lowest = v
	if first:
		raise ValueError("values must contain at least one element")
	return lowest



def get_highest_list_value(values):
	first = True
	highest = None
	for v in values:
		if first:
			highest = v
			first = False
		else:
			if v > highest:
				highest = v
	if first:
		raise ValueError("values must contain at least one element")
	return highest