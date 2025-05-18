def cribaEra(n, esPri):  
     
    esPri[0] = esPri[1] = False
    for i in range(2, n+1): 
        esPri[i] = True
  
    p = 2
    while(p*p <= n):    
         
        if (esPri[p] == True):         
             
            i = p*p 
            while(i <= n): 
                esPri[i] = False
                i += p 
        p += 1         
 
def sumaPar(n):  
     
    esPri = [0] * (n+1) 
    cribaEra(n, esPri)   
  
    for i in range(0, n): 
      
        if (esPri[i] and esPri[n - i]): 
          
            print(i," + ",(n - i)) 
            return
            
    print("0","+", "0")               

N=int(input(" Digite el valor de N :"))

if (N==2):
    print("El valor de N Debe ser mayor a 2")    
else:
    sumaPar(N) 