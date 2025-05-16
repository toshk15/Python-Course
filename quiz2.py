def findFirstAndLast(arr,n,x):

	first=-1
	last=-1

	for i in range(0,n):
		if(x!=arr[i]):
			#print(x)
			continue

		if(first==-1):
			first=i
			print("fisrt", first)
		last=i
		print("last", last)

	if(first!=-1):
		print("first index= ", first,
			"\nlast index= ", last)
	else:
		print("no encontramos nada")

arr = [1,2,2,2,2,3,4,7,8,8]
n=len(arr)
x=2
findFirstAndLast(arr,n,x)
