class Stack:

	def __init__(self):
		self.items = []

	def is_empty(self):
		return self.items == []

	def push(self, item):
		self.items.insert(0, item)

	def pop(self):
		return self.items.pop(0)

	def peek(self):
		return self.items[0]

	def size(self):
		return len(self.items)

#s = Stack()
#s.push('hello')
#s.push("fernando")
#print(s.pop())

def par_checker(symbol_string):
	s = Stack()
	balanced=True
	index = 0
	while index<len(symbol_string) and balanced:
		symbol = symbol_string[index]
		print("simbolo:", symbol)
		if symbol == "(":
			s.push(symbol)
			print("pila:", symbol)
		else:
			if s.is_empty():
				balanced = False
			else:
				s.pop()
				print("pila 2:", s)
		index = index + 1

	if balanced and s.is_empty():
		return True
	else:
		return False
print(par_checker('((()))'))
print(par_checker('(()'))

