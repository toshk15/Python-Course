class A:
    
    def __init__(self):
        self.test=0
        
    def add(self,x,y):
        x.test+=1
        y+=1
        return (x.test+y)
        #print(x.test+y)
        

a=A()
z=A()
b=0

#print(z.add(a,b))

for i in range(0,25):
    z.add(a,b)
print(z.add(a,b))
