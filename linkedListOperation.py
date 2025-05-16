
#creamos un nodo
class Node():

	def __init__(self, data):

		self.data = data
		self.next = None
#union del nodo con next
class LinkedList():

	def __init__(self):
		self.head = None

	def tamanoLista(self):
		nodoActual = self.head
		length = 0
		while nodoActual is not None:
			length+=1
			nodoActual = nodoActual.next
		return length

	def listaVacia(self):
		if self.head is None:
			return True
		else:
			return False



	def insertarNodoIncio(self, nuevo_nodo):

		nodoTemporal = self.head
		self.head = nuevo_nodo
		self.head.next = nodoTemporal
		del nodoTemporal



	def insertar(self, nuevo_nodo):

		if self.head is None:
			self.head = nuevo_nodo
		else:
			ultimoNodo = self.head
			while True:
				if ultimoNodo.next is None:
					break
				ultimoNodo = ultimoNodo.next
			ultimoNodo.next = nuevo_nodo

	def insertarPos(self, nuevo_nodo, posicion):

		if posicion < 0 or posicion>= self.tamanoLista():
			print("posicion invalida")
			return

		if posicion is 0:
			self.insertarNodoIncio(nuevo_nodo)
			return

		nodoActual = self.head
		posicionActual = 0
		while True:
			if posicionActual == posicion:
				nodoPrevio.next = nuevo_nodo
				nuevo_nodo.next = nodoActual
				break
			nodoPrevio = nodoActual
			nodoActual = nodoActual.next
			posicionActual+=1

	def eliminarInicio(self):
		if self.listaVacia is False:
			inicioPrevio = self.head
			self.head = self.head.next
			inicioPrevio.next = None
		else:
			print("Lista vacia no hay nada que eliminar")

	def eliminarUltimo(self):
		ultimoNodo = self.head
		while ultimoNodo.next is not None:
			nodoPrevio = ultimoNodo
			ultimoNodo = ultimoNodo.next
		nodoPrevio.next = None

	def eliminarPosicion(self, posicion):
		if posicion < 0 or posicion >= self.tamanoLista():
			print("posicion invalida")
			return
		if self.listaVacia() is False:
			if posicion is 0:
				self.eliminarInicio()
				return
		nodoActual = self.head
		posicionActual= 0
		while True:
			if posicionActual == posicion:
				nodoPrevio.next = nodoActual.next
				nodoActual.next = None
				break
			nodoPrevio = nodoActual
			nodoActual = nodoActual.next
			posicionActual+=1

		

	def imprimirLista(self):

		if self.head is None:
			print("lista vacia")
			return
		nodoActual = self.head
		while True:
			if nodoActual is None:
				break
			print(nodoActual.data)
			nodoActual = nodoActual.next




#nodo=>data, next
#nodo1.data=>"almareli, nodo1.next=>none"
nodo1 = Node("Almareli")
miLista = LinkedList()
miLista.insertar(nodo1)
nodo2 = Node("Fernando")

miLista.insertar(nodo2)
nodo3 = Node("Mora")

miLista.insertar(nodo3)

nodo4 = Node("Maluko")
miLista.insertarNodoIncio(nodo4)

#nodo5 = Node("Extraño")
#miLista.insertarPos(nodo5, 2)(

#miLista.eliminarUltimo()
miLista.eliminarPosicion(2)


miLista.imprimirLista()