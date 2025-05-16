X = [[1,2,3], 
    [4 ,5,6], 
    [7 ,8,9]] 
  
Y = [[9,8,7], 
    [6,5,4], 
    [3,2,1]] 

#print(len(X)) 
print(X[0])
print(X[1])
print(X[2])
  
result = [[0,0,0], 
        [0,0,0], 
        [0,0,0]] 
  
# iterate through rows 
for i in range(len(X)):
#    print(len(X))    
# iterate through columns 
    for j in range(len(X[0])):
#        print(len(X[0])) 
        result[i][j] = X[i][j] + Y[i][j] 
  
for r in result: 
    print(r) 