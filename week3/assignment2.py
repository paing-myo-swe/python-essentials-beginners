# Program: Sum of All Digits
# A number as input to calculate sum of the 5 digits in that number

num = list(input("Enter a 5 digits number:"))

while(len(num) != 5):
    num = list(input("Invalid input, Please enter a number with 5 digits long:"))
else:
    i = 0
    sum = 0
    while(i < len(num)):
        sum += int(num[i])
        i += 1
    else:
        print("Sum of all digits is", sum)