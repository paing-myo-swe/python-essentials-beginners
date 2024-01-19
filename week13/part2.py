def evenOrOdd(num):
    if(num % 2 == 0):
        return "even"
    return "odd"

print(evenOrOdd(2))
print(evenOrOdd(5))

def fun1(x, y = 30):
    print(x,",",y)

fun1(15)

def name(firstName, lastName):
    print(firstName,lastName)

name(lastName="Smith", firstName="John")

def fun3(*args):
    for arg in args:
        print(arg)


fun3("Hello", "World", "Python")

def fun4(**args):
    for key, value in args.items():
        print(key,":", value)
    
fun4(first="Hello",mid="World",last="Python")