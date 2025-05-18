class A:

	def metodo01(self, i = None):
		if i is None:
			print("Secuencia 01")

		else:
			print("Secuencia 02")
			return 1

def main():
	x = A()
	x.metodo01()
	ret = x.metodo01(5)
	print(ret)


if __name__ =="__main__":
	main()
