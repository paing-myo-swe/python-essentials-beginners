import os, shutil

fileName = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test.txt')

#shutil.copyfile(fileName, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'copyed.txt'))

#shutil.copy(fileName, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'copyed.txt'))

shutil.copy2(fileName, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'copyed.txt'))