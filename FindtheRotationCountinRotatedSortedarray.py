def countRotation(arr, n):

	min=arr[0]
	print(min)
	for i in range(0,n):
		#print(arr[i])

		if (min > arr[i]):
			min=arr[i]
			#print(min)
			min_index= i
			#print(min_index)
	return min_index;


arr = [15, 18, 2, 3, 6, 12]
n=len(arr)
print(countRotation(arr, n))


if (15 > 15):
	print("true")
else:
	print("false")