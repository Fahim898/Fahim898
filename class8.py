"""
-list -> [data1,data2, data3,.....]
-tuple
-set
-dictionary
"""

variable_list = [10,12,11,13,15,14,18,1,81,'Fahim',]

print(variable_list[2])

for value in variable_list :
    print("{}".format(value),end="")

print(variable_list[0:9])

for data in variable_list:
    if data == 11 or data == 13:
        print(data)

variable_list.reverse()
print(variable_list)

print(variable_list[::-1])