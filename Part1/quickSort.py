def particion(arr, low, high):
	i=(low-1)
	pivot = arr[high]

	for j in range(low, high):

		if arr[j] < pivot:
			i+=1
			arr[i], arr[j]= arr[j], arr[i]
	arr[i+1],arr[high] = arr[high], arr[i+1]
	return (i+1)


def quickSort(arr, low, high):
	if low < high:
		pi = particion(arr, low, high)
		print("este es el valor de particion: ", pi)

		quickSort(arr, low, pi-1)
		quickSort(arr, pi+1, high)

arr=[10,80,30,90,40,50,70]
n=len(arr)
quickSort(arr,0,n-1)
print("el array en orden es: ")
for i in range(n):
	print("%d" %arr[i]),