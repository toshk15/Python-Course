class Elemento(object):

	def __init__(self, valor):

		self.valor = valor
		self.next = None



class LinkedList(object):

	def __init__(self, head=None):
		self.head = head

	def append(self, nuevo_elemento):
		current = self.head
		if (self.head):
			while current.next:
				current = current.next
			current.next = nuevo_elemento
		else:
			self.head = nuevo_elemento

	def get_posicion(self, posicion):
		current = self.head
		contador = 1

		while contador <= posicion and current:
			if contador == posicion:
				return current
			current = current.next
			contador+=1

		return None

	def insert(self, nuevo_elemento, posicion):
		if posicion > 1:
			posicion_objetivo = self.get_posicion(posicion-1)
			nuevo_elemento.next = posicion_objetivo.next
			posicion_objetivo.next = nuevo_elemento
		else:

			nuevo_elemento.next = self.head
			self.head = nuevo_elemento

	def eliminar(self, valor):
		current = self.head
		previo = None
		while current:
			if current.valor == valor:
				if not previo:
					self.head = current.next
					return True
				else:
					previo.next = current.next
					return True
			previo = current
			current = current.next
		return False

	def insertar_primero(self, nuevo_elemento):
		nuevo_elemento.next = self.head
		self.head = nuevo_elemento
		return self

	def eliminar_primero(self):
		if self.head:
			eliminado = (self.head)
			self.head=self.head.next
			eliminado.next = None
			return eliminado


ligaJusticia = LinkedList()
nodo1 = Elemento("Superman")
nodo2 = Elemento("Batman")
nodo3 = Elemento("Goku")
nodo4 = Elemento("Bulma")
node5 = Elemento("Intruso")
node6 = Elemento("Picoro")
node7 = Elemento("Fernando")
node8= Elemento("Almareli")

ligaJusticia.append(nodo1)
ligaJusticia.append(nodo2)
ligaJusticia.append(nodo3)
ligaJusticia.append(nodo4)

ligaJusticia.insert(node5, 3)
ligaJusticia.insert(node6, 4)

ligaJusticia.insertar_primero(node7)
ligaJusticia.insertar_primero(node8)

ligaJusticia.insertar_primero(node7)
ligaJusticia.insertar_primero(node8)

#print(ligaJusticia.get_posicion(1).valor)
#print(ligaJusticia.get_posicion(2).valor)

print(ligaJusticia.eliminar_primero().valor)
print(ligaJusticia.get_posicion(2).valor)

print(ligaJusticia.get_posicion(1).valor)


ligaJusticia.eliminar("Picoro")


print(ligaJusticia.eliminar("Picoro"))



