# find() is return first founded index

words = "Welcome to Python Basic Course"

result = words.find("Basic")
print("Basic is found at index", result)

result = words.find("Hello")
print("Hello is not contain, so return", result)

result = words.find("course")
print("find() is case sensitive, so return", result)

if(words.find("Python") != -1):
    print("Pyhton is contain")
else:
    print("Python is not found")