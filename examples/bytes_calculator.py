import math

sizeInBytes = float(input("Enter file size as Bytes"))

sizeInKB = 1024
sizeInMB = math.floor(sizeInKB * sizeInKB)
sizeInGB = sizeInMB * sizeInKB
sizeInTB = sizeInGB * sizeInGB

if(sizeInBytes < sizeInMB):
    print("%.2f" % (sizeInBytes / sizeInKB),"KB")
elif(sizeInBytes < sizeInGB):
    print("%.2f" % (sizeInBytes / sizeInMB),"MB")
elif(sizeInBytes < sizeInTB):
    print("%.2f" % (sizeInBytes / sizeInGB),"GB")
