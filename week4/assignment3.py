# Program: Fibonacci Series

number = int(input("Enter a number:"))

print(number,"Fibonacci numbers are:", end = "")

num1 = 0
num2 = 1
count = 0
next = num2

while(count < number):
    count += 1
    print(next, end = ",")
    num1 = num2
    num2 = next
    next = num1 + num2
    