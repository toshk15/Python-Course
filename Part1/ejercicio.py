#_list = ['he', 'ha', 'hi']
#for i in range(1,10):
#	for x in _list:
#		print(x*i)


#numbers=[15,21,42]
#factors=[]
#for num in numbers:
#	for x in range(1,num+1):
#		if num%x==0:
#			factors.append(x)
#	print(num,factors,end=',')

#a=[]
#for i in range(11):
#	a.append('hello')
#	for j in range(i):
#		a[i]+="."
#for k in range(11):
#	print(a[k])

#x=['ab','cd']
#for i in x:
#	print(x)

'''def narci(num):
	suma=[]
	numero=len(str(num))
	potencia=int(numero)
	digitos=[int(i) for i in str(num)]
	for i in digitos:
		produ=i**potencia
		suma.append(produ)
		sumTotal=sum(suma)
		#print("suma :", sumTotal)
	if(sumTotal==num):
		print(str(num), "es un numero narcistico")
	else:
		print(str(num), "no es un numero narcistico")

narci(153)
'''
'''def eliVocales(string):
	frase=string
	vocales =('A', 'a', 'E', 'e', 'I', 'i','O','o','U','u')
	return ''.join([x for x in frase if x not in vocales])

print(eliVocales("This website is for losers LOL!"))
'''

'''
def Descending_Order(num):
    return int("".join(map(str, sorted([i for i in str(num)], reverse=True))))


print(Descending_Order(1234))

'''

'''
import math
def narcissistic( value ):
    power = len(str(value))
    sum = 0
    for x in str(value):
        #sum+=math.pow(int(x), power)
        p=int(x)**power
        sum+=p
    if sum == value:
        return True
    else:
        return False

print(narcissistic(153))
'''

 
'''
def numRev(n):
	rev = 0
	x=str(n)
	lista=[]
	lista[:0]=x
	#print(lista)
	lista2=sorted(lista)
	#print(lista2)
	newList=''.join(str(ele) for ele in lista2)
	#print(newList)
	n=int(newList)
	while(n > 0):
		a = n % 10
		rev = rev * 10 + a
		n = n // 10
	return rev 
  
print(numRev(9775420))
'''
'''
s="banana"
for x in s:
  print(x)


a = "Hello, World!"
print(len(a))
'''

'''	
def strings(s1, s2):
	sf1=''
	sf2=''
	sf3=''
	for i in s1:
		c=0
		for j in s2:
			if(i==j):
				c=c+1
				continue
		if(c==0):
			sf1+=str(i)

	for i in s2:
		c=0
		for j in s1:
			if(i==j):
				c=c+1
				continue
		if(c==0):
			sf2+=str(i)
	return sf1+sf2

	



s1="xyab"
s2="xzca"

print(strings(s1, s2))
'''

'''
def solve(a,b):
    s = set(a)&set(b)
    #print(s)
    #t=a+b
    #print(t)
    return ''.join(c for c in a+b if c not in s)	


s1="xyab"
s2="xzca"

print(solve(s1, s2))		
			
'''	
'''
def re(num):
	
	n=str(num)
	if(len(n)==1):
		
		return 0
	else:
		
		p=1
		s=str(num)
		for i in s:
			p*=int(i)
			#print(p)
		return re(p)+1


print(re(4))

'''
'''
def persistence(n):
    n = str(n)
    count = 0
    while len(n) > 1:
        p = 1
        for i in n:
            p *= int(i)
            print(p)
        n = str(p)
        count += 1
    return count

print(persistence(39))

'''
'''
num =str(4358)
largest = ''.join(sorted(num)[::-1])#get the largest
second_largest = largest[:-2] + largest[-1:-3:-1]
print('largest number: ', largest)
print('second largest number: ', second_largest)

print(largest[-1:-3:-1])
'''
'''
def decryptString(str, n): 
      
    i = 0
    jump = 1
    decryptedStr = "" 
  
    while (i < n): 
        decryptedStr += str[i]; 
        i += jump 
        print("i", i)  
        jump += 1
        print("jump", jump)
  
    return decryptedStr 
  
# Driver code 
if __name__ == '__main__': 
    str = "geeeeekkkksssss"
    n = len(str) 
    print(decryptString(str, n)) 

'''
'''
def encryptString(string, n):  
  
    i, cnt = 0, 0
    encryptedStr = ""  
  
    while i < n:


  
        # Number of times the current  
        # character will be repeated  
        cnt = i + 1
        print("i", i)
        print("cnt", cnt)
  
        # Repeat the current character  
        # in the encrypted string  
        while cnt > 0:  
            encryptedStr += string[i] 
            print("encryptedStr", encryptedStr)
            cnt -= 1
              
        i += 1
  
    return encryptedStr  
  
# Driver code  
if __name__ == "__main__": 
  
    string = "geeks"
    n = len(string)  
    print(encryptString(string, n)) 
  
'''

# # Python3 implementation of the above approach:
# MAX = 26
 
# # Function to return the encrypted strring
# def encryptstrr(strr, n, x):
     
#     # Reduce x because rotation of
#     # length 26 is unnecessary
#     x = x % MAX
#     #print("x :", x)
#     arr = list(strr)
     
#     # calculate the frequency of characters
#     freq = [0]*MAX
#     #print("freq :", freq)
#     for i in range(n):
    	
#     	freq[ord(arr[i]) - ord('a')] += 1
#     	#print("valor: ",freq)

     
#     for i in range(n):
         
#         # If the frequency of current character
#         # is even then increment it by x
#         #print("valor: ",freq)
#         if (freq[ord(arr[i]) - ord('a')] % 2 == 0):
#             pos = (ord(arr[i]) - ord('a') + x) % MAX
#             arr[i] = chr(pos + ord('a'))
         
#         # Else decrement it by x
#         else:
#             pos = (ord(arr[i]) - ord('a') - x)
#             if (pos < 0):
#                 pos += MAX
#             arr[i] = chr(pos + ord('a'))
             
#     # Return the count
#     return "".join(arr)
 
 
# # Driver code
# s = "abcda"
# print("a :",ord(s[0]))
# print("b :",ord(s[1]))
# print("c :",ord(s[2]))
# print("d :",ord(s[3]))
# print("y :",ord('y'))
# print("z :",ord('z'))

# n = len(s)
# x = 3
# print(encryptstrr(s, n, x))

# points = 174

# if points <= 50:
#     result = "Congratulations! You won a wooden rabbit!"
# elif points <= 150:
#     result = "Oh dear, no prize this time."
# elif points <= 180:
#     result = "Congratulations! You won a wafer-thin mint!"
# else:
#     result = "Congratulations! You won a penguin!"

# print(result)

# names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# for name in names:
#     name = name.lower().replace(" ", "_")

# print(names)

# tokens = ['<greeting>', 'Hello World!', '</greeting>']
# count = 0

# for i in tokens:
#     if "<" in i:
#         count+=1

# print(count)
"""
result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

for key, value in basket_items.items():
	if key in fruits:
		result+=value
	
print(result)
"""

def search2d(mat, num):

	m, n = len(mat), len(mat[0])
	l , r = 0, (m*n - 1)

	while l <= r:

		mid = (l + r) // 2

		target = mat[mid//n][mid%n]

		if target == num:
			return True

		elif target < num:
			l = mid + 1
		else:
			r = mid - 1
	return False


mat = [[1,2,3], [4,5,6], [7,8,9]]
print(search2d(mat, 0))