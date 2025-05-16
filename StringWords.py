# Returns count of words with frequency 
# exactly 2. 
def countWords(stri, n): 
    m = dict() 
    for i in range(n): 
        m[stri[i]] = m.get(stri[i],0) + 1
        print(m)
   
    res = 0
    for i in m.values(): 
        if i == 2: 
            res += 1
   
    return res 
   
# Driver code 
s = [ "hate", "love", "peace", "love", 
      "peace", "hate", "love", "peace", 
                "love", "peace" ] 
n = len(s) 
print(countWords(s, n)) 