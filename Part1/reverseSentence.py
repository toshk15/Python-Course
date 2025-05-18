# Python3 implementation of the approach  
  
# Function to reverse the words  
# of the given sentence  
def reverse(k): 
    # Create an empty character array stack  
    s = []  
    token = k.split() 

    print("token", token)
      
    # Push words into the stack  
    for word in token : 
        s.append(word); 
        print("PALABRAS:", s)

          
    while (len(s)) : 
        # Get the words in reverse order  
        print(s.pop(),end= " ");
        #print("WORDS:", s)      
  
# Driver code  
if __name__ == "__main__" :  
  
    k = "Fernando Rojas Ramos";  
    reverse(k);  