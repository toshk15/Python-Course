#a=[1,3,5,7]
#b=a
#c=[1,3,5,7]

#print(b)

#print(a is b, a==c, a is c)

#d={0:"a", 1: "b",2:"c"}
#for x in d.keys():
#	print(d[x])

# nums=[42,8,3,17,8]
# nums.remove(8)
# nums.sort()
# print(nums)

# print(''.join(str(nums)[1:-1]))

# nota=input("introduce nota")

# def eva(nota):
# 	valo="perfecto"

# 	if nota<10:
# 		valo="casi perfecto"
# 		if nota<9:
# 			valo="puedes hacerlo mejor"
# 	return valo

# eva(nota)

# square_dict = dict()
# for num in range(1, 11):
# 	square_dict[num]=num*num
# print(square_dict)

# square_dict = {num:num*num for num in range(1,11)}
# print(square_dict)

old_price={'milk':1.02, 'coffe': 2.5, 'bread': 2.5}
dollar_to_pound = 0.76
new_price={item:value*dollar_to_pound for(item, value) in old_price.items()}
print(new_price)