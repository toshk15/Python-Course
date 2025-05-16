# Python3 program to reverse the  
# number using a stack 
  
# Stack to maintain order of digits 
st = []; 
  
# Function to push digits into stack 
def push_digits(number): 
  
    while (number != 0):  
        st.append(number % 10); 
        print("variable st", st)
        number = int(number / 10); 
       # print("variable number", number)
  
# Function to reverse the number 
def reverse_number(number): 
      
    # Function call to push number's  
    # digits to stack 
    push_digits(number); 
      
    reverse = 0; 
    i = 1; 
      
    # Popping the digits and forming  
    # the reversed number 
    while (len(st) > 0):  
        reverse = reverse + (st[len(st) - 1] * i);
        print("reverse=", reverse) 
        st.pop(); 
        print("valor de st dentro del ciclo", st)
        i = i * 10; 
      
    # Return the reversed number formed 
    return reverse; 
  
# Driver Code 
number = 123; 
  
# Function call to reverse number 
print(reverse_number(number)); 