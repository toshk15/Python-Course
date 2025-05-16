

import random
F = int(input("Numero de Filas :")) 
C = int(input("Numero de columnas :")) 
  
# Initialize matrix 
matrix=[]
matrix1=[]
matrix2=[]
sumMatrix= []


def crearMatrix(matrix):
    
    for i in range(F):
        a =[]
        for j in range(C):
            a.append(random.randint(1,10))
        matrix.append(a) 

def crearMatrixResultado(matrix):
    
    for i in range(F):
        a =[]
        for j in range(C):
            a.append(0)
        matrix.append(a) 

def mostrarMatrix(matrix):
    for i in range(F):
        for j in range(C):
            print(matrix[i][j], end = " ")
        print() 


  
def mostrarSum(sumMatrix, matrix1, matrix2):
    for i in range(F):
        for j in range(C):
            sumMatrix[i][j]=matrix1[i][j]+matrix2[i][j]
    for r in sumMatrix:
        print(r)
        print() 

crearMatrix(matrix1)
print("-----------MATRIZ 1-----------")
mostrarMatrix(matrix1)

crearMatrix(matrix2)
print("-----------MATRIZ 2-----------")
mostrarMatrix(matrix2)

crearMatrixResultado(sumMatrix)

print("----SUMA DE MATRIZ1 + MATRIZ2--------")
mostrarSum(sumMatrix, matrix1, matrix2)
