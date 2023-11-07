str1 = "Hello World"

print(str1.ljust(30))
print(str1.ljust(30,'*'))

print(str1.rjust(30))
print(str1.rjust(30,'*'))

print(str1)

str2 = '{:#<30}'.format(str1)
print(str2)
str2 = '{:#>30}'.format(str1)
print(str2)
str2 = '{:#^30}'.format(str1)
print(str2)

s1 = "Left Alignment"
s2 = "Right Alignment"
s3 = "Center Alignment"

print(f"{s1 : <30}")
print(f"{s2 : >30}")
print(f"{s3 : ^30}")
print(f"{s1 : <30}{s3 : ^30}{s2 : >30}")

print()

products = ["Dell","Acer","Lenovo"]
prices = [580,640,700]
qty = [23,45,31]

print(f"{'Product Name' : <20}{'Price' : ^10}{'Qty' : >5}\n")
print('-' * 35)

for i in range(0,len(products)):
    print(f"{products[i] : <20}{prices[i] : ^10}{qty[i] : >5}")