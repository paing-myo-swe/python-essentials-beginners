import time

t = (2024,1,16,8,57,30,4,294,0)

l = time.mktime(t)
print(l)

a = time.asctime(t)
print(a)

localTime = time.localtime()
print(localTime)

f = time.strftime("%d/%m/%Y %H:%M:%S", localTime)
print(f)

s = "Fri Jan 16 08:57:30 2024"
p = time.strptime(s, "%a %b %d %H:%M:%S %Y")
print(p)