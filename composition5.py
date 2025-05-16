                                                                                                                                                                                                                                                           
class Bateria():
	def __init__(self):
		self.pcBateria = 100
		self.gasto = 0.9

	def Uso(self):
		self.pcBateria = self.pcBateria * self.gasto
		#print(self.pcBateria, self.gasto)
		self.getBateriaMala()

	def getBateriaMala(self):
		print("Tiene " + str(self.pcBateria) + "% de bateria")
		if (self.pcBateria < 55):
			print("bateria baja")
			return True
		else:
			return False


class Teclado():

	def __init__(self):

		self.valor1 = 0
		self.valor2 = 0

	def valorEntrada(self, v1, v2):
		self.valor1 = v1
		self.valor2 = v2

	def getValor(self):

		return [self.valor1, self.valor2]

class UnidadLogica():

	def suma(self, valores):
		val = 0
		for v in valores:
			val = val + v
		return val

	def resta(self, valores):
		val = 0 
		for v in valores:
			val = val - v

		return val


class Display():

	def __init__(self):
		self.brillo = 20
		self.texto = "0"

	def mostrarTexto(self, texto):
		self.texto = texto
		print(self.texto)

class Calculadora():

	def __init__(self):
		self.bateria = Bateria()
		self.entrada = Teclado()
		self.operacion = UnidadLogica()
		self.display = Display()


	def nuevaOperacion(self, valor1, valor2):
	
		self.entrada.valorEntrada(valor1, valor2)
		self.bateria.Uso()

	def suma(self):
		suma = self.operacion.suma(self.entrada.getValor())
		self.display.mostrarTexto(suma)
		self.bateria.Uso()



CALL = Calculadora()

CALL.nuevaOperacion(10, 20)

CALL.suma()

CALL.nuevaOperacion(15, 20)

CALL.suma()

CALL.nuevaOperacion(20, 20)

CALL.suma()

