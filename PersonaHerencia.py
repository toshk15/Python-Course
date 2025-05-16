class Persona:

	def __init__(self, nombre, apellido):
		self.nombre = nombre
		self.apellido = apellido

	def imprimirNombre(self):

		print(self.nombre, self.apellido)

class Estudiante(Persona):
	def __init__(self, nombre, apellido):
		pass


ale = Estudiante("Ale", " Rpjas")
ale.imprimirNombre()

Fer = Persona("Fernando", "Rojas")
Fer.imprimirNombre()
