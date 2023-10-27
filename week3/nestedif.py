num = int(input("Enter a number"))

if((num % 2) == 0):
    if((num % 3) == 0):
        print("This number is divisible by both 2 and 3")
    else:
        print("This number is divisible by 2 but not divisible by 3")
elif((num % 3) == 0):
    print("This number is divisible by 3 but not divisible by 2")
else:
    print("This number is not divisible by both 2 and 3")