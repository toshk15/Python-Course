class Car:
	def __init__(self, brand, color):
		self.brand = brand
		self.color = color

	def __repr__(self):
		return 'My car is {} and was produced by {}'.format(self.color, self.brand)


myCar = Car('Corsa','Blanco')

print(myCar)