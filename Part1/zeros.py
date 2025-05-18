# Python3 code to move all zeroes 
# at the end of array 

def pushZerosToEnd(arr, n): 
    count = 0      

    for i in range(n): 
        if arr[i] != 0: 
              
            # here count is incremented 
            arr[count] = arr[i] 
            #print(arr[count])
            count+=1
            #print(count)

    while count < n: 
        arr[count] = 0
        #print(arr[count])
        count += 1
        print(count)
          
# Driver code 
arr = [8, 0, 0, 0, 6, 0, 9] 
n = len(arr) 
pushZerosToEnd(arr, n) 
print("Array after pushing all zeros to end of array:") 
print(arr) 