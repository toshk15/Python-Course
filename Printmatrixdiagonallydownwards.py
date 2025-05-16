def printMatrixDiagonallyDown(matrix,n):

	for k in range(n):

		row=0
		col=k

		while (col>=0):
			print("ciclo1")
			print(matrix[row][col], end = " ")
			row+=1
			col-=1
			print("columna primer ciclo", col)


	for j in range(1,n):

		col = n-1
		row = j

		while(row < n):
			#print("ciclo2")
			print(matrix[row][col], end = " ")
			row +=1
			col -=1
if __name__=='__main__':

	matrix = [[1,2,3], [4,5,6], [7,8,9]]
	n=3
	printMatrixDiagonallyDown(matrix,n)