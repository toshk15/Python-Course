#mylist = ['geeks','forgeeks']
#for i in mylist:
#    i.upper()
#print(mylist)

#mylist = ['geeks', 'forgeeks']
#for i in mylist:
#    mylist.append(i.upper())
#print(mylist)

#i = 1
#while True:
#    if i % 7 == 0:
#        break
#    print(i)
#    i += 1
    

my_string = "geeksforgeeks"
i = "i"
while i in my_string: 
    print(i, end =" ") 
    


a = {i: i * i for i in range(6)}
print(a)

a = {1: i*i for i in range (6)}
print(a)



dictionary1 = {'Google' : 1, 
               'Facebook' : 2, 
               'Microsoft' : 3
               } 
dictionary2 = {'GFG' : 1, 
               'Microsoft' : 2, 
               'Youtube' : 3
               } 
dictionary1.update(dictionary2); 
for key, values in dictionary1.items(): 
    print(key, values) 



temp = dict() 
temp['key1'] = {'key1' : 44, 'key2' : 566} 
temp['key2'] = [1, 2, 3, 4] 
for (key, values) in temp.items(): 
    print(values, end = "") 



print(['love', 'python'][bool('gfg')]) 

print(['love', 'python'][bool(0)]) 



print ('\x25\x26')

