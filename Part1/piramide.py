class Poligono:
	def __init__(self, num_de_lados):
		self.n = num_de_lados
		self.lados = [0 for i in range(num_de_lados)]
	def entradaLados(self):
		self.lados = [float(input("dame el lado " +str(i+1)+" : ")) for i in range(self.n)]
	def dispLados(self):
		for i in range(self.n):
			print("Lados", i+1, "es",self.lados[i])

class Triangulo(Poligono):
	def __init__(self):
		Poligono.__init__(self,3)
	def encontrarArea(self):
		a, b, c = self.lados
		s=(a + b + c)/2
		area = (s*(s-a)*(s-b)*(s-c))**0.5
		print("Area: " + area)
t = Triangulo()
t.entradaLados()
