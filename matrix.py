#valores=[5,10,12,13]
#aux=[]
#for i in valores:	
#	if i<=10:
#		aux.append(i)
#print(aux)

import random
filas= int(input("Numero de filas: "))
columnas= int(input("Numero de columnas: "))

def matriz1(filas, columnas, valor=None):
	m=[]
	for i in range(filas):
		m.append([])
		for y in range(columnas):
			m[i].append(random.randint(1,10))
	return m
def recorrerMatriz1(m):
	for i in m:
		for j in i:
			print(j, end=" ")
			print("")

ma1= matriz1(filas, columnas)
recorrerMatriz1(ma1)

def matriz2(filas, columnas, valor=None):
	m=[]
	for i in range(filas):
		m.append([])
		for j in range(columnas):
			m[i].append(random.randint(1,10))
	return m
print("\n")

def recorrerMatriz2(m):
	for i in m:
		for j in i:
			print(j, end=" ")
			print("")

ma2= matriz1(filas, columnas)
recorrerMatriz2(ma2)
print("\n")

matriz3=[]
def sumaMatrices(matriz1, matriz2):
	global matriz3
	for i in range(filas):
		for j in range(columnas):
			matriz3[[i][j]]= matriz1[[i][j]]+ matriz2[[i][j]]
	return matriz3

print("RESULTADO")
print(matriz3)

