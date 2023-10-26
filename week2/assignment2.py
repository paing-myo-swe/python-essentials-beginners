# Checking whether the number is in a list or not

try:
    num = int(input("Enter a number "))

    myList = [100,101,102,103,104,105,106,107,108,109,110]

    if(num in myList):
        print(num,"is in 100-110")
    else:
        print(num,"is not in 100-110")

except ValueError:
    print("Enter a valid number")