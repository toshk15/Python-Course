class Fecha():
	"""docstring dia, mes, ano Fecha"""
	def __init__(self):

		self.dia = 0
		self.mes = 0
		self.ano = 0

	def setFecha(self, dia, mes, ano):

		self.dia = dia
		self.mes = mes
		self.ano = ano

	def ImprimirFecha(self):

		print(self.dia, self.mes, self.ano)

#class Persona(object):
class Persona():


	def __init__(self):


		self.fecha = Fecha()

	def setPersona(self, nombre, cumple):

		self.nombre = nombre
		self.fecha = cumple

	def MostrarCumple(self):

		print(self.nombre)
		self.fecha.ImprimirFecha()



cumpleanos = Fecha()
cumpleanos.setFecha(29, 4, 1990)

fer = Persona()
fer.setPersona("fernando", cumpleanos)
fer.MostrarCumple()






		