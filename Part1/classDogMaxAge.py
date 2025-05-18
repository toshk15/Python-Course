class Dog():
	species = 'mammal'

	def __init__(self, name, age):
		self.name = name
		self.age = age

malek = Dog("malek", 6)
malina = Dog("malina", 3)
maluko = Dog("maluko", 1)

def get_biggest_age (*args):
	return max(args)


print("the oldest dog is {} years old.".format(get_biggest_age(malek.age, malina.age, maluko.age)))







