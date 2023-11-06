# Program: Counting uppercas,lowercase,space and Swapping case of input String

str1 = input("Enter a sentence:")

upperCaseCount = 0
lowerCaseCount = 0
spaceCount = 0
i = 0

while(i < len(str1)):
    if(str1[i].isspace()):
        spaceCount += 1
    elif(str1[i].isupper()):
        upperCaseCount += 1
    else:
        lowerCaseCount += 1
    i += 1

print("Total uppercase is:", upperCaseCount)
print("Total lowercase is:", lowerCaseCount)
print("Total space is:", spaceCount)
print("Swapped Case format is:", str1.swapcase())