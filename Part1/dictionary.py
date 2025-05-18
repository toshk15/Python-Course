#marbles = {"red" : 34,"green" : 30, "brown" : 31, "yellow" : 29}

#print(marbles.get("orange"))

#print(marbles.get("orange", 0))

#marbles.update({"orange":34, "blue":23, "purple": 36})

#print(marbles)

#print(marbles.keys())

#print(marbles.values())

#print(marbles.items())

animals = ['cat', 'dog', 'goldfish', 'canary', 'cat']

animals_set = set(animals)

#print(animals_set)

animals_unique_list = list(animals_set)

#print("list", animals_unique_list)

animals_unique_tuple = tuple(animals_unique_list)

#print("tuple", animals_unique_tuple)

#other exercises

marbles = {"red": 34, "green": 30, "brown": 31, "yellow": 29 }

colours = list(marbles) # the keys will be used by default

print(colours)

counts = tuple(marbles.values()) # but we can use a view to get the values

print(counts)

marbles_set = set(marbles.items()) # or the key-value pairs

print(marbles_set)

dict([(1, 2), (3, 4)])
print(dict)

