arr1=[]
arr2=[]

def creArray(arr, n):    
    for x in range(n):
        x=int(input("Digite los numeros del vector : "))
        arr.append(x)
    print(arr)
    return arr

def compArrays(arr1, arr2, n):
    for i in range(n):
        if arr1[i]>arr2[i]:
            if (i==n-1):
                print("1")
        else:
            print("0")
            break       
    return

n=int(input("digite el tamaño del vector : "))

creArray(arr1,n)
creArray(arr2,n)
compArrays(arr1, arr2, n)



    



