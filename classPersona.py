class Person:
	def __init__(mysillyobject, name, age):
		mysillyobject.name = name
		mysillyobject.age = age

	def myfunc(abc):
		print( "hello my name is", abc.name,"con mi edad", abc.age)

p1 = Person("Fernando", 29)

p1.myfunc()
