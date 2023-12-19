tuple1 = (23,4,45,676,88,221,44)
tuple2 = ("apple","banana","orange","mango","banana")

print(max(tuple1))
print(min(tuple1))
print(len(tuple1))
print(sum(tuple1))

print(max(tuple2))
print(min(tuple2))
print(len(tuple2))

list1 = [21,3,34,466,75]
tuple3 = tuple(list1)

print(tuple3)
print(tuple1.index(4))
print(tuple2.index("orange"))
print(tuple2.count("banana"))