tuple1 = ('a','b','c','d')
tuple2 = 'a','b','c','d','1','2','3'
tuple3 = ('a',1,10.5,'hello',['a','b','c'])
tuple4 = (('a','b','c'),(1,3,5),[2,4,6],"hello world")

print(tuple1 + tuple2)
print(tuple1 * 3)
print(tuple3[1:3])
print("hello" in tuple3)
print("hello world" not in tuple3)

for i in tuple4:
    print(i,end="")
    print(type(i))