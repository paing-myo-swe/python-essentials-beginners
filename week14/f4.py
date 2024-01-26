import os

fileName = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'f4.txt')

file1 = open(fileName,'a+')

newLine = "Hello World"
file1.write(newLine)
file1.close()

