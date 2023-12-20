# Distance between two points is the length of the line segment 
# that connects the two points in a plane. The formula to find the distance between 
# the two points is usually given by d=√((x2 – x1)² + (y2 – y1)²).  
# This formula is used to find the distance between any two points on a coordinate plane or x-y plane.

import math
# x1 and y1 are orginal point
x1 = 0
y1 = 0

x2 = 2
y2 = 2

d = math.sqrt(pow((x2 - x1),2) + pow((y2 - y1),2))
print(d)

o = [x1,y1]
p = [x2,y2]

# Calculate Euclidean distance
print (math.dist(o, p))

