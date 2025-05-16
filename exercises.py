# copiar una cadena en otro array

#def myCopy(s1, s2):

#	for i in range(len(s1)):
#		s2[i] = s1[i];

#s1 ="FERNANDO";
#s2 = [""]*(len(s1));
#myCopy(s1,s2);
#print(("".join(s2)));
  
#///////////////////////////////////////////////

#def myCopy(s1, s2, index): 
      
    # copying each character from s1 to s2  
 #   s2[index] = s1[index]; 
 #   print(s2[index], s1[index]);
  
    # if string reach to end then stop  
 #   if (index == len(s1) - 1): 
 #       return; 
  
    # increase character index by one  
 #   myCopy(s1, s2, index + 1); 
  
# Driver Code  
#if __name__ == '__main__': 
#    s1 = "GEEKSFORGEEKS";

#    s2 = [0] * (len(s1)); # crea array del tamaño de s2 con ceros

#    print(s2); 
#    index = 0; 
#    myCopy(s1, s2, index); #pasamos arrays a la funcion 
#    print("".join(s2));



#///////////////////////////////////////////////////////

#def recursiveReverse(str):
#	stack = []

#	for i in range(len(str)):
#		stack.append(str[i])

#		print(str[i])

#	for i in range(len(str)):
#		str[i] = stack.pop()
#		print(str[i])

#if __name__ == "__main__":

#	str = "FERNANDO"

#	str = list(str)
#	recursiveReverse(str)
#	str = str
#	str = ''.join(str)
	
#	print(str)

#///////////////////////////////////////////////////////

#def reverseStr(str): 
#    n = len(str) 
      
    # initialising a empty 
    # string 'str1' 
#    str1 = '' 
#    i = n - 1
    #print(i)
#    while i >= 0:    	

#        str1 += str[i]
#        print(str1) 
#        i -= 1
#    print(str1)      
  
# Driver Code 

#def main(): 
#    str = "FERNANDO"; 
#    reverseStr(str); 
      
#if __name__=="__main__": 
#    main()      

#///////////////////////////////////////////////////////


  
# Function to reverse a string 
# def reverseStr(str): 
#     n = len(str) 
  
#     i, j = 0, n-1
  
    # Swap character starting from 
    # two corners 
#    while i < j: 
#        str[i], str[j] = str[j], str[i] 
  
#        i += 1
#        j -= 1
  
  
# Driver code 
#if __name__ == "__main__": 
#    str = "FERNANDO"
  
    # converting string to list 
    # because strings do not support 
    # item assignment 
#    str = list(str) 
#    reverseStr(str)   
    # converting list to string 
#    str = ''.join(str)   
#    print(str) 

#///////////////////////////////////////////////////////  

#def toDecimal(binary, i = 0): 
  
    # If we reached last character  
#    n = len(binary)  
    #print(n)
#    if (i == n - 1) : 
#        return int(binary[i]) - 0
      
    # Add current tern and recur for  
    # remaining terms 

    #print(int(binary[i]))
    #

#    z=(int(binary[i]) - 0) << (n - i - 1)
#    y=(1<<3)

#    print(y)

#    x=(((int(binary[i]) - 0) << (n - i - 1)) + toDecimal(binary, i + 1)) 


  


    #print (((int(binary[i]) - 0) << (n - i - 1)))
#    return x
# Driver code  
#if __name__ == "__main__" : 
      
#    binary = "1010"
#    print(toDecimal(binary)) 


#///////////////////////////////////////////////////////
#def decToBinary(n):

#	binaryNum = [0] * n;

#	print(binaryNum)

#	i = 0;
#	while(n>0):

#		binaryNum[i] = n%2; 
#		print(binaryNum[i])
#		n = int(n/2);
#		print(n)
#		i+=1;


#	for j in range(i-1, -1, -1):
#		print(j)
#		print(binaryNum[j], end="");

#n = 13;
#decToBinary(n);



#demostracion de los operadores de residuo y division normal.
#numero = 17
#numero2 = numero%2
#print(numero2)



# Python program to 
# decrement with 
# range() 
  
# incremented by -2 y limite de la lista a 5
#for i in range(25, 5, -2): 
#    print(i, end =" ") 
#print() 
  
# incremented by -4 y limite de la lista a 9
#for i in range(30, 9, -4): 
#    print(i, end =" ") 
#print() 
  
# incremented by -3 y limite de la lista -6
#for i in range(25, -6, -3): 
#    print(i, end =" ") 
#i=4
#for j in range(i-1, -1, -1):
#	print(j, end =" ")

# Function that convert  
# Decimal to binary 
#def decToBinary(n): 
      
    # Size of an integer is 
    # assumed to be 32 bits 
#    for i in range(3, -1, -1):  
#        k = n >> i; 
#        print(k)
#        if (k & 1):  
#            print("1", end = ""); 
#        else: 
#            print("0", end = ""); 
  
# Driver Code 
#n = 13; 
#decToBinary(n); 
#print("\n")059


#num=13
#num2 = num>>3
#print(num2)

#if (num2 & 1):
#	print("uno");
#else:
#	print("quien sabe")

#def find(decimal_number):
#	if decimal_number==0:
#		return 0
#	else:
#		return (decimal_number % 2 + 10 * find(int(decimal_number //2)))

#decimal_number = 10
#print(find(decimal_number))

#///////////////////////////////////////////////////////

# Function to check sum of 
# digit using recursion

#def sum_of_digit(n): 
#    if n == 0: 
#        return 0
#    return (n % 10 + sum_of_digit(int(n / 10))) 
  
# Driven code to check above 
#num = 123
#result = sum_of_digit(num) 
#print("Sum of digits in",num,"is", result) 


#///////////////////////////////////////////////////////
  
# Python program to reverse a  
# stack using recursion 
  
# Below is a recursive function  
# that inserts an element 
# at the bottom of a stack. 

#def insertAtBottom(stack, item): 
#    if isEmpty(stack):
#    	push(stack, item) 
#    	print("item", item)
#    	print("stackkkkkkkk", stack)
#    else: 

#        temp = pop(stack)
#        print("temporal con stack no vacia", temp) 
#        insertAtBottom(stack, item) 
#        push(stack, temp) 
  
# Below is the function that  
# reverses the given stack 
# using insertAtBottom() 
#def reverse(stack): 
	


#    if not isEmpty(stack):

#        print("original pila", stack)
#        temp = pop(stack) 

#        print("temporal variable", temp)
#        print("stack", stack)
#        reverse(stack) 
#        print("despues de funcion reverse", stack)
#        insertAtBottom(stack, temp)         
  
#def createStack(): 
#    stack = [] 
#    return stack 
  
# Function to check if  
# the stack is empty 
#def isEmpty( stack ): 
#    return len(stack) == 0
  
# Function to push an  
# item to stack 
#def push( stack, item ): 
#    stack.append( item ) 
#    print(stack)
  
# Function to pop an  
# item from stack 
#def pop( stack ): 
  
    # If stack is empty 
    # then error 
#    if(isEmpty( stack )): 
#        print("Stack Underflow ") 
#        exit(1) 
  
#    return stack.pop() 
  
# Function to print the stack 
#def prints(stack): 
#    for i in range(len(stack)-1, -1, -1): 
#        print(stack[i], end = ' ') 
#    print() 
  
# Driver Code 
  
#stack = createStack() 
#push( stack, str(4) ) 
#push( stack, str(3) ) 
#push( stack, str(2) ) 
#push( stack, str(1) ) 
#print("Original Stack ") 
#prints(stack) 
  
#reverse(stack) 
  
#print("Reversed Stack ") 
#prints(stack) 

#///////////////////////////////////////////////////////

# Python program to sort a stack using recursion 
  
# Recursive method to insert element in sorted way 
def sortedInsert(s , element): 
      
    # Base case: Either stack is empty or newly inserted 
    # item is greater than top (more than all existing) 
    if len(s) == 0 or element > s[-1]: 
        s.append(element)
        print("primer element", s)
        return
    else: 
          
        # Remove the top item and recur 
        temp = s.pop() 
        print("Que tiene la variable temporal S?", s)
        sortedInsert(s, element) 
  
        # Put back the top item removed earlier 
        s.append(temp) 
        print("final", s)
  
# Method to sort stack 
def sortStack(s): 
      
    # If stack is not empty 
    if len(s) != 0: 
          
        # Remove the top item 
        temp = s.pop() 

        print("imprimiendo las variables temporales", temp)
        print("imprimiendo la pila", s)
          
        # Sort remaining stack 
        sortStack(s) 
          
        # Push the top item back in sorted stack 
        sortedInsert(s , temp) 

  
# Printing contents of stack 
def printStack(s): 
    for i in s[::-1]: 
            print(i , end=" ") 
    print() 
      
# Driver Code 
if __name__=='__main__': 
    s = [ ] 
    s.append(30) 
    s.append(-5) 
    s.append(18) 
    s.append(14) 
    s.append(-3)
    print("Primera seccion del stack \n", s)
  
    print("Stack elements before sorting: ") 
    printStack(s) 
  
    sortStack(s) 
  
    print("\nStack elements after sorting: ") 
    printStack(s) 