# Swap Two Numbers Program without Using Temp variable
num1 = 10
num2 = 20

print("Swap Two Numbers Program without Using Temp variable")

print("Before swapping.....")
print("Num 1 is", num1)
print("Num 2 is", num2)

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print("After swapping.....")
print("Num 1 is", num1)
print("Num 2 is", num2)