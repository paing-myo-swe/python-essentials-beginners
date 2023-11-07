import re

str1 = "This is a pyhton basic course"
str2 = "apple,orange,mango,banana"
str3 = "one:two:three"
str4 = "Sun and Mon and Tue and Wed and Thu and Fri and Sat"
str5 = "Hello World\nPython for Begineer"
str6 = "Hello World\nPython for Begineer\tWeek 6"

print(str1.split())
print(str2.split(','))
print(str3.split(':',2))
print(str4.split('and'))
print(str5.split('\n'))

print(re.split('\n|\t', str6))