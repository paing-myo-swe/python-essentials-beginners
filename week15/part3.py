import os, shutil

fileName = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test.txt')

#os.rename(fileName, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'renamed-test.txt'))

#os.remove(fileName)

shutil.move(fileName, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'moved.txt'))