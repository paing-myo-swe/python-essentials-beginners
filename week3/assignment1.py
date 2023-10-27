# Check a number Even or Odd using Nested if

num = int(input("Enter a number: "))

if((num % 2) == 0):
    if(num > 20):
        print("It is a even number and it is also greater than 20.")
    else:
        print("It is a even number and it is also less than 20.")
else:
    if(num > 20):
        print("It is a odd number and it is also greater than 20.")
    else:
        print("It is a odd number and it is also less than 20.")