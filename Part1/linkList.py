#insertar nodos LinkList
class Node:
	#Funcion para inicializar el nodo objeto
	def __init__(self, data):
		self.data = data # assignacion de data
		self.next = None # inicializar el proximo como nulo
# Clase LinkList contiene un nodo objeto
class LinkList:
	#funcion para inicializar head
	def __init__(self):
		self.head = None

	#Funcion para insertar un nuevo nodo en el principio

	def push(self, new_data):
		# 1 & 2 colocan el nodo y ponen en data
		new_node = Node(new_data)
		#hacer proximo de un nodo como head
		new_node.next = self.head
		#mueve la cabeza para apuntar a el nuevo nodo
		self.head = new_node

	# esta funcion esta en la LinkList, inserta un nuevo nodo despues del previo asignado,
	#este metodo esta definido dentro LinkList que se muestra abajo

	def insertAfter(self, prev_node, new_data):
		#checa si dado un previo nodo dado
		if prev_node is None:
			print("the given previous node must in LinkList")
			return
	#crea un nuevo nodo y pone en data

		new_node = Node(new_data)

	#hacer next el nuevo nodo como porximo del previo nodo

		new_node.next = prev_node.next

	#hacer next de previo nodo como el nuevo nodo

		prev_node.next = new_node

	#esta funcion esta definida en LinkList, anexa un nuevo nodo al final, 
	#este metodo esta definido dentro LinkList se muestra abajo

	def append(self, new_data):
		#crear un nuevo nodo
		#poner en data
		#asignar next como None
		new_node = Node(new_data)

		#si LinkList esta vacia , entonces hacemos que el el nuevo nodo sea la cabecera

		if self.head is None:
			self.head = new_node
			return
		#sino atraviesa hasta el final de la lista
		last = self.head
		while (last.next):
			last = last.next
		#cambia next como el ultimo
		last.next = new_node

	# utiliza la funcion para imprimir la lista
	def printList(self):
		temp = self.head
		while (temp):
			print(temp.data)
			temp = temp.next
#Ejecucion empieza aqui
if __name__=='__main__':
	#empieza con una lista vacia
	llist = LinkList()
	#inserta 6 link list recibe 6
	llist.append(6)
	#insertar 7 en el principio 
	llist.push(7)
	#inserta 1 en el principio
	llist.push(1)
	#inserta 4 al final de la lista
	llist.append(4)
	#insertar 8 y despues 7, link list obtiene 1, 7, 8, 6, 4, None
	llist.insertAfter(llist.head.next,8)
	print("Created Linked list is:", llist.printList())