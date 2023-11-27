# rindex() is return last founded index
# rindex() raises ValueError: when it is not found

words = "Welcome to Python Basic Course! I Love Python"

result = words.rindex("Python")
print("Python found at", result)

result = words.rindex("PHP")
print("PHP is not found, so return ValueError", result)