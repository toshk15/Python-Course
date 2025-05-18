
# Python program to sort  
# string of characters using stack   
  
def printSorted(s, l):  
      
    stack =[]  
   
    tempstack =[]        
      
    stack.append(s[0]) 

    print("PILA", s)          
 
    for i in range(1, l): 
          
        # i-th character ASCII  
        a = ord(s[i]) 
        print("a del ciclo", a)  
        b = ord(stack[-1])
        print("b del ciclo", b)
        print("Primeros elementos agregados a la pila", stack)
          
        # if greater or equal to top element  
        # then push to stack  
        if((a-b)>= 1 or (a == b)): 
            stack.append(s[i])  
            print("Elementos en la pila guardados:", stack)
              
        # if smaller, then push all element  
        # to the temporary stack  
        elif((b-a)>= 1): 
              
            # push all greater elements  
            while((b-a)>= 1): 

                print("pila al iniciO en el ciclo b - a :", stack)
                  
                # push operation  
                tempstack.append(stack.pop()) 

                print("Pila temporal dentro del ciclo b - a!", tempstack)
                print("Pila Stack dentro del ciclo b - a!", stack)
                  
                # push till the stack is not-empty  
                if(len(stack)>0): 
                    b = ord(stack[-1]) 
                    print("ciclo horrible", b)
                    print("tamaño de la stack", len(stack))
                else: 
                    break
                      
            # push the i-th character  
            stack.append(s[i]) 
            print("Pila despues del break del ciclo:", stack)
              
            # push the tempstack back to stack  
            while(len(tempstack)>0): 
                print("tamaño de la pila temporal:", len(tempstack))
                stack.append(tempstack.pop()) 
                print("se guarda valor de pila temporal en PILA:", stack) 
                  
    # print the stack in reverse order  
    print(''.join(stack))  
  
  
# Driver Code 
s = "cba" 
l = len(s) 
printSorted(s, l) 

print("----------------------------------------------------------- \n")

a0 = ord(s[0])
print("c", a0)
a1 = ord(s[1])
print("b", a1)
a2 = ord(s[2])
print("a", a2)







#a0 = ord(s[0])
#print("f", a0)
#a1 = ord(s[1])
#print("e", a1)
#a2 = ord(s[2])
#print("r", a2)
#a3 = ord(s[3])
#print("n", a3)
#a4 = ord(s[4])
#print("a", a4)
#a5 = ord(s[5])
#print("n",a5)
#a6 = ord(s[6])
#print("d", a6)
#a7 = ord(s[7])
#print("o",a7)