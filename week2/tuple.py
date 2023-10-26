# Tuple can not be modify, it is immutable
tuple1 = ("Python", 777, 10.0, 50, 'Hello')

print(tuple1)

tuple2 = [12345, 'Program']

print(tuple2)

print(tuple1[0])
print(tuple1[1:4])
print(tuple1[1:])
print(tuple1 * 4)