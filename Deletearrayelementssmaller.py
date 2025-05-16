# Function to delete elements 
def deleteElements(arr, n, k): 
      
    # create an empty stack st 
    st = [] 
    st.append(arr[0]) 
    print(st)      
  
    top = 0
    count = 0
  
    for i in range(1, n):           
    
        while(len(st) != 0 and count < k 
                   and st[top] < arr[i]):
            #print(st[top]) 
            st.pop() 
            count += 1
            top -= 1
            #print(top)
  
        st.append(arr[i])
        
        top += 1
  
    # print the remaining elements 
    for i in range(0, len(st)): 
        print(st[i], " ", end="") 
  
# Driver code 
k = 2
arr = [20, 10, 25, 30, 40]  
deleteElements(arr, len(arr), k) 