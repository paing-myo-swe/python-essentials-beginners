import random

mylist = []

for i in range(0, 15):
    mylist.insert(i, random.randint(1, 100))

print(mylist)
print("Total elements is", len(mylist))
print("Min value is", min(mylist))
print("Max value is", max(mylist))