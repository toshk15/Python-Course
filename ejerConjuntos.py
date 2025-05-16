print("Descuentos de Estacionamiento")
costo1 = int(input())
costo2= int(input())
costo3= int(input())
print("Primer Intervalo")
l1 = int(input())
l2= int(input())
a = []
for i in range(l1, l2+1):
    a.append(i)
#print(a)    
    
print("Segundo Intervalo")
l3 = int(input())
l4= int(input())
b = []
for i in range(l3, l4+1):
    b.append(i)
#print(b)   

print("Tercer Intervalo")
l5 = int(input())
l6= int(input())
c = []
for i in range(l5, l6+1):
    c.append(i)
#print(c)  


# Python program to illustrate the intersection 
# of 3 lists using set() method 
def intersection(a1, b1, c1): 
    return list(set(a1) & set(b1)& set(c1)) 

I1=intersection(a, b, c)
if len(I1)>0:
    cF1 = (len(I1)-1)*3*costo1
else:
    cF1 = 0

#print("Costo final 1: ", cF1)
#print("intersection 3 set", I1)


def Diff(set1, set2):
    I1_dif = [i for i in set1 + set2 if i not in set1 or i not in set2]
    return I1_dif

I1diff1=Diff(a, I1)
I1diff2=Diff(b, I1)
I1diff3=Diff(c, I1)
#print("Diferencia de a-I1 : ", I1diff1)
#print("Diferencia de b-I1 : ", I1diff2)
#print("Diferencia de c-I1 : ", I1diff3)

def intersection2(a1, b1): 
    return list(set(a1) & set(b1))


I2=intersection2(I1diff1, I1diff2)
I3=intersection2(I1diff1, I1diff3)
I4=intersection2(I1diff2, I1diff3)

#print("I2 : ", I2)
#print("I3 : ", I3)
#print("I4 : ", I4)

def Union(lst1, lst2):
    final_list = list(set(lst1) | set(lst2)) 
    return final_list 

U1=Union(I2, I3)
U2=Union(U1, I4)

#print("union 1 : ", U1)
#print("union 2: ", U2)

n = len(U2)
def sucess(U2):
    for t2 in range(n-1):
        if U2[t2]+1 == U2[t2+1]:
            F2 = (len(U2)-1)*2*costo2
            return F2
        else:
            F2 = (len(U2))*2*costo2
            return F2       
    

cF2 = sucess(U2)

#print("Costo final 2: ", cF2)

if len(I1diff1)!=0:
    I1diff4=Diff(I1diff1,U2)
else:
     I1diff4=[] 
if len(I1diff2)!=0:
    I1diff5=Diff(I1diff2,U2)
else:
     I1diff5=[] 

if len(I1diff3)!=0:
    Inter=intersection2(I1diff3, U2)
    #print("Inter",Inter)

    if len(Inter)==0:
        I1diff6=I1diff3
    else:
        I1diff6=Diff(I1diff3,U2)
     
else:
    I1diff6=[] 

#print("Diferencia de I1diff4 : ", I1diff4)
#print("Diferencia de I1diff5 : ", I1diff5)
#print("Diferencia de I1diff6 : ", I1diff6)

U3=Union(I1diff4, I1diff5)
U4=Union(U3, I1diff6)

U4Test = U4[:] 
U4Test.sort() 
if (U4Test == U4):
    cF3 = (len(U4)-1)*costo3
else:
    cF3 = (len(U4))*costo3   
      
 

#print("union 3: ", U4)


#print("Costo final 3: ", cF3)

costoFinal = cF1 + cF2 +cF3
print("Costo Final : ", costoFinal)