# This method uses the spherical law of cosines, which is a trigonometric formula that 
# calculates the great-circle distance between two points on the Earth’s surface. It’s 
# simpler than Haversine but may be less accurate for long distances due to floating-point rounding errors.

from math import radians, sin, cos, acos
 
print("Input coordinates of two points:")
mlat = radians(float(input("Location 1 latitude: ")))
mlon = radians(float(input("Location 2 longitude: ")))
plat = radians(float(input("Location 1latitude: ")))
plon = radians(float(input("Location 2 longitude: ")))
 
dist = 6371.01 * acos(sin(mlat)*sin(plat) + cos(mlat)*cos(plat)*cos(mlon - plon))
print("The distance is %.2fkm." % dist)

# We convert the coordinates from degrees to radians and use the sine and cosine functions along with 
# the Earth’s mean radius (6371.01 km) to calculate the distance. The acos() function is used to compute 
# the arccosine of the central angle between the two locations.

# sin(mlat) is the sine of the latitude of a location m
# sin(plat) is the sine of the latitude of another location p
# cos(mlat) is the cosine of the latitude of location m
# cos(plat) is the cosine of the latitude of location p
# cos(mlon - plon) is the cosine of the difference between the longitudes of the two locations
# The expression (sin(mlat)*sin(plat) + cos(mlat)*cos(plat)*cos(mlon - plon)) calculates the cosine of the central angle between the two locations
# acos() is used to calculate the arccosine of the central angle
# 6371.01 is the mean radius of the Earth in kilometers.