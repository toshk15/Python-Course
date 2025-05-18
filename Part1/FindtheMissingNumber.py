#def getMissingNo(A):
#	n=len(A)
#	total=(n+1)*(n+2)/2
#	sumA=0
#	for i in A:
#		sumA+=i
#		numMissing=total-sumA

#	return numMissing

#A= [1,2,4,5,6]
#miss = getMissingNo(A)
#print(miss)


def  getMissingNo(a,n):
	i, total = 0, 1

	for i in range(2, n+2):
		#print("numero en el range",i)
		total+=i #2+1, 3+2, 4+3, 5+4, 
		print("total + i = ",total)
		total-=a[i-2] #  
		print("total - a = ",total)
	return total

arr = [1,2,3,5]
print(getMissingNo(arr, len(arr)))

