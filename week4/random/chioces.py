# randomly select multiple elements

import random

seq1 = ["apple","banana","orange","mango"]

seq2 = [1,2,3,4,5,6,7,8,9]

seq3 = (10,20,30,40,50,60,70,80)

print(random.choices(seq1,k = 3))
print(random.choices(seq2,k = 3))
print(random.choices(seq3,k = 3))