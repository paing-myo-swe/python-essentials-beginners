import os

fileName = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'f3.txt')

file1 = open(fileName,'w+')

lines = ["Hello Python\n", "This is Python\n", "Welcome to Python\n"]
file1.writelines(lines)
file1.close()

