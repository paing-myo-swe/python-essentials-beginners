str1 = "Hello"
str2 = "world!"
str3 = " "

print("String concatenation by using + =>",str1 + str3 + str2)

print("String concatenation by using .join() method =>","".join(str1 + str3 + str2))

print("String concatenation by using .format() method => {}{}{}".format(str1,str3,str2))

print("String concatenation by using f string =>",f'{str1},{str3},{str2}')