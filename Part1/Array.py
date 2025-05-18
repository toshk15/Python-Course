arr=[]
pos=[]
neg=[]

def creaArray(arr):
    for x in range(0,21):
        x=int(input("Digite sus numeros : "))
        if x==0:
            break
        else:
            arr.append(x)
            #print(arr)
    return arr

def creaArrayPosNeg(arr):
    n=len(arr) 
    for i in range(n):
        if arr[i]>0:
            pos.append(arr[i]) 
        else:
            neg.append(arr[i]) 
    return pos,neg    
       

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] 
  
# Main

creaArray(arr)

pos, neg = creaArrayPosNeg(arr)

bubbleSort(pos)

print ("Positivos:") 
for x in range(len(pos)): 
    print ("%d" %pos[x])

bubbleSort(neg)

print ("Negativos:") 
for x in range(len(neg)): 
    print ("%d" %neg[x])  


