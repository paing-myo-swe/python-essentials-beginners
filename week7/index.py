# index() is return first founded index
# index() raises ValueError: when it is not found

words = "Welcome to Python Basic Course! I Love Python"

result = words.index("Python")
print("Python found at", result)

result = words.index("PHP")
print("PHP is not found, so return ValueError", result)