amount = int(input("Enter amount"))
discount = 0

if(amount < 1000):
    discount = amount * 0.05
elif(amount > 1000 and amount < 5000):
    discount = amount * 0.10
else:
    discount = amount * 0.15

print("Discount", discount)
print("Net payable amount", amount - discount)