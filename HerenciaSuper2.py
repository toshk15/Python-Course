class Person(object):

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __str__(self):
        return self.first + " " + self.last + ", " + str(self.age)


class Employee(Person):
    
    def __init__(self, first, last, age, sal):        
        super(Employee, self).__init__(first, last, age)
        self.sal = sal

    def __str__(self):
        return super(Employee,self).__str__() + ", " + str(self.sal)



def main():
    x = Person("Ashwin", "Pajankar", 31)
    print(x)

    y = Employee("James", "Bond", 40, 1000)
    print(y)

if __name__ == "__main__":
    main()

