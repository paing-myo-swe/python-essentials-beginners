a = 20
b = 20
c = 10

print("a =", a, ":", id(a))
print("b =", b, ":", id(b))
print("c =", c, ":", id(c))

if(a is b):
    print("a and b are same identity")

if(a is not c):
    print("a and c are not same identity")