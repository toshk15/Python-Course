class Dog():
	species = 'mammal'

	def __init__(self, name, age):
		self.name = name
		self.age = age

malina = Dog("malina", 2)
maluko = Dog("maluko", 1)

print("{} is {} and {} is {}.".format(malina.name, malina.age, maluko.name, maluko.age))

if malina.species == "mammal":
	print("{0} is a {1}!".format(malina.name, malina.species))



