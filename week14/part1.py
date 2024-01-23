import os

fileName = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'demo.txt')

file1 = open(fileName,'r')

#print(file1.read())

print(file1.readline())

print(file1.readlines())

file1.close()