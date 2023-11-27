list1 = [[1,2,3],[4,5,6]]

print(list1)
print(list1[0])
print(list1[1])

list1[0][1] = 0
list1[1][1] = 0

print(list1[0])
print(list1[1])

list1[0].append(5)
list1[1].append(8)

print(list1[0])
print(list1[1])

print(list1)