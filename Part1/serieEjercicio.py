class Sec():
	def __init__(self, base, patron):
		self.base=base
		self.patron=patron


	def serie(self, n):
		self.n=n
		for i in range(1, n+1):
			print(self.base+(i-1)*self.patron)

b=int(input("Digite el valor de la base : "))
p=int(input("Digite el valor de la patron : "))
x=Sec(b,p)
t=int(input("Digite el numero de Terminos : "))
x.serie(t)
