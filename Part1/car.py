class CarRecord:
    def __init__(self):
        self.year = 0
        self.carVin=''
    
    def __str__(self):        
        return 'Year: '+str(self.year)+', VIN: '+(self.carVin)


myCar = CarRecord()
myCar.year=int(input())
myCar.carVin=input()

print(myCar)