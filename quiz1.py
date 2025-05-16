#i = 5

#while True:
#	if i%9==0:
#		break
#	print(i)
#	i+=1


class solution(object):
	def twoSum(self, nums, target):

		num_to_index={}

		for i, num in enumerate(nums):
			#print("i, num", i, num)
			print("valor de target", target)

			if target - num in num_to_index:
				print("entro al ciclo target-num", target-num)
				return [num_to_index[target-num], i]
			num_to_index[num]=i
			print("i", i)
			print("num_to_index",num_to_index[num])


		return[]

x =[1,2,3,4,5,6]

y = solution()

z=y.twoSum(x,6)

print(z)
