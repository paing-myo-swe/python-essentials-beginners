title = "Welcome to PHP Basic Course! I Love PHP...PHP...PHP"

result = title.replace("PHP", "Python")
print(result)

result = title.replace("Basic Course", "")
print(result)

result = title.replace("...", ", ")
print(result)

result = title.replace("HP", " ", 2) #(old,new,count)
print(result)