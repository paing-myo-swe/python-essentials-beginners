try:
    num = int(input("Enter a number "))

    if(num > 0):
        print("It is a positive number.")
    elif(num < 0):
        print("It is a nagative number.")
    else:
        print("It it a zero.")
    
except ValueError:
    print("Enter a valid number")