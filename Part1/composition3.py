class Fecha:
	"""docstring dia, mes, ano Fecha"""
	def __init__(self, dia, mes, ano):

		self.dia = dia
		self.mes = mes
		self.ano = ano



	def ImprimirFecha(self):

		print(self.dia, self.mes, self.ano)

#class Persona(object):
class Persona:


	def __init__(self, nombre, dia, mes, ano):

		self.nombre = nombre
		self.obj_fecha = Fecha(dia, mes, ano)



	def MostrarCumple(self):

		print(self.nombre)
		self.obj_fecha.ImprimirFecha()





fer = Persona("Fernando", 1, 2, 1990)
fer.MostrarCumple()







		