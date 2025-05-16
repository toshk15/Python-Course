class Dog():
	species = 'mammal'

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def description(self):
		return "{} is {} years old".format(self.name, self.age)

	def speak(self, sound):
		return "{} says {}".format(self.name, sound)
 

class chihuahua(Dog):
 	def run(self, speed):
 		return "{} runs {}".format(self.name, speed)

class bulldog(Dog):
 	def run(self, speed):
 		return "{} runs {}".format(self.name, speed)


malina = bulldog("malina", 6)
print(malina.description())

print(malina.run("fast"))




