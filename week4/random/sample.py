# randomly select multiple elements

import random

seq1 = ["apple","banana","orange","mango"]

seq2 = [1,2,3,4,5,6,7,8,9]

seq3 = (10,20,30,40,50,60,70,80)

print(random.sample(seq1,3))
print(random.sample(seq2,3))
print(random.sample(seq3,3))