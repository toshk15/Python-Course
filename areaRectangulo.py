class rectangle():
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length
    def area(self):    	
    	a = self.breadth * self.length
    	return a
    def perimetro(self):
    	p = 2*self.breadth+2*self.length
    	return p
        #return self.breadth*self.length
a=int(input("Enter length of rectangle: "))
b=int(input("Enter breadth of rectangle: "))
obj=rectangle(a,b)
print("Perimetro del rectangulo: ", obj.perimetro())
print("Area of rectangle:",obj.area())
 
print()