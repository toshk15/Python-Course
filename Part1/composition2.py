def find_next_square(sq):
	root = sq**0.5
	if root.is_integer():
		return (root + 1)**2
	return -1

x = find_next_square(121)
print(x)