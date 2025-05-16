 
# Function that returns true if the word is found 
def isWordPresent(sentence, word): 
      
    s = sentence.split(" ") 
    print("Split:", s)
  
    for i in s:  
       
        if (i == word): 
            return True
    return False
  
s = "Car in Car"
word = "Car"
  
if (isWordPresent(s, word)): 
    print("Yes") 
else: 
    print("No") 
  