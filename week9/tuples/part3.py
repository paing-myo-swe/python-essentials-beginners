tuple1 = ('a','b','c','d')
tuple2 = (1,2,3,4,5)
tuple3 = ((1,3,5),(2,4,6))

print(max(tuple1))
print(min(tuple2))
print('e' in tuple1)
print(3 in tuple2)

for i in tuple3:
    for j in i:
        print(j)