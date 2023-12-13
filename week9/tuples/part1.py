# tuple is immutable and it can store different data types

tuple1 = ('a','b','c','d')
tuple2 = 'a','b','c','d','1','2','3'
tuple3 = ('a',1,10.5,'hello',['a','b','c'])
tuple4 = (('a','b','c'),(1,3,5),[2,4,6],"hello world")

print(tuple1)
print(tuple2)
print(tuple3)
print(tuple4)

print(tuple1[1])
print(tuple2[-1])
print(tuple4[0][1])
print(tuple4[1][1])

del(tuple3)
print(tuple3)