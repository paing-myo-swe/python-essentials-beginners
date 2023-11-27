# rfind() is return last founded index

words = "Welcome to Python Basic Course! I Love Python"

result = words.rfind("Python")
print("Python found at", result)

result = words.rfind("PHP")
print("PHP is not found, so return", result)