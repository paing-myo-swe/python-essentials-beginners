mylist = []

for i in range(3):
    list1 = []
    for j in range(3):
        num = int(input("Enter a number:"))
        list1.append(num)
    mylist.append(list1)
    
print(mylist)

for i in range(3):
    for j in range(3):
        print(mylist[i][j], end=" ")
    print("")