# Discount Calculation

try:
    amount = int(input("Enter amount "))
    discount = 0

    if(amount < 1000):
        discount = amount * 0.05
    else:
        discount = amount * 0.10
        
    print("You have discount:ß", discount)
    print("Net payable amount:", amount - discount)

except ValueError:
    print("Enter valid amount")