mylist = [1,2,4,5,7,12,32,26,17,18,28]

try:
    num = int(input("Enter a number: "))
    if(num in mylist):
        print("The element contains in the list.")
    else:
        print("The element does not contains in the list.")
except ValueError:
    print("Please enter a valid number")


