# Bitwises are used in integer value

a = 60 # 60 = 00111100
b = 13 # 13 = 00001101

print("a =",a,":", bin(a))
print("b =",b,":", bin(b))

c = 0
c = a & b
print("result of a & b is", c, ":", bin(c))

c = a | b
print("result of a | b is", c, ":", bin(c))

c = a ^ b
print("result of a ^ b is", c, ":", bin(c))