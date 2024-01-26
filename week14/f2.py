import os

fileName = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'f1.txt')

file1 = open(fileName,'w+')

file1.write("Hello Python")
file1.close()

