# Program: Multiplication Table

number = int(input("Enter a number for multiplication table:"))

i = 1

for i in range(11):
    print(number,"x",i,'=', number * i)
