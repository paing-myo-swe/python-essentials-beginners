import copy

list1 = ["cat","bat","get","set","jet","bat","cat","set","get"]
list2 = [1,3,5,7,9,7,2,4,6,8]

print(list1)
print(list2)

list3 = list1.copy()
list3[8] = "mad"
list4 = copy.deepcopy(list2)

print(list3)
print(list4)