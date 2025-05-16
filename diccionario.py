a = {} 
a[1] = 1
print(a)
a['1'] = 2
print(a)
a[1]= a[1]+1
print(a)
count = 0
for i in a:   
    count += a[i] 
    print(a[i])
    
print(count) 
