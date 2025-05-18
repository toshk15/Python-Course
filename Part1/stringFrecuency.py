sentence = "Nobody expects the spanish inquisition"
sentence = sentence.lower().replace(" ","")
dictionary = {}

for i in sentence:
    try:
        dictionary[i]+=1
    except:
        dictionary[i] = 1
        sorted_dictionary = {}
        sorted_keys = sorted(dictionary, key = dictionary.get, reverse = True)
        for k in sorted_keys:
            sorted_dictionary[k] = dictionary[k]
print(sorted_dictionary)
        