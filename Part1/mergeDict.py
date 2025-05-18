from collections import defaultdict

input1 = [{'roll_no' : ['123445','1212'], 'school_id':1}, {'roll_no':['HA-4848231'], 'school_id':2}]

input2 = [{'roll_no':['473427'], 'school_id': 2}, {'roll_no': ['092112'], 'school_id':5}]

temp = defaultdict(list)

for elem in input1:
    temp[elem['school_id']].extend(elem['roll_no'])
    
for elem in input2:
    temp[elem['school_id']].extend(elem['roll_no'])
output = [{"roll_no": y, "school_id":x} for x, y in temp.items()]
print(output)