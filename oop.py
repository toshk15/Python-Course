#class Producto:

#	def __init__(self, producto, precio, unidades):
#
#		self.producto = producto
#		self.precio= precio
#		self.unidades= unidades
#	def costo_total(self):
#		costo = self.precio* self.unidades
#		return costo

#mi_objeto_producto = Producto("corbata", 35, 67)

#print(mi_objeto_producto.producto)
#print(mi_objeto_producto.precio)
#print(mi_objeto_producto.unidades)
#print(mi_objeto_producto.costo_total())

#class Producto:
#	def __init__(self,producto, precio, unidades):
#
#		self.producto = producto
#		self.precio = precio
#		self.unidades = unidades

#	def __costo_total(self):
#		costo = self.precio * self.unidades
#		return costo

#	def nuevo_precio(self, precio):
#		self.precio = precio
#
#	def agrega(self, cantidad):
#		self.unidades = self.unidades + cantidad
#	
#	def saca(self, cantidad):
#		if cantidad <= self.unidades:
#			self.unidades = self.unidades - cantidad
#		else:
#			print("no hay suficientes")

#	def informe(self):
#		print("Producto: " + self.producto)
#		print("Precio: " + str(self.precio))
#		print("Unidades: " + str(self.unidades))
#		print("Precio Total: " + str(self.__costo_total()))

#mi_producto1 = Producto("pantalon", 100, 6)
#mi_producto2 = Producto("camiseta", 50, 5)

#print(mi_producto1.precio)
#print(mi_producto2.unidades)
#mi_producto2.agrega(5)
#print(mi_producto2.unidades)
#mi_producto2.informe()


class Animal:
	def __init__(self, nombre, patas):

		self.nombre=nombre
		self.patas=patas

	def saluda(self):
		print("El animal llamado " + str(self.nombre) + " saluda")


class Perro(Animal):

	def ladra(self):
		print("guau guau")

mi_mascota = Perro("Maluko", 4)
mi_mascota.saluda()
mi_mascota.ladra()

