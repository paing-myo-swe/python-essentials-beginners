myBook = {
    "title": "Pyhton",
    "description": "This is Python Book",
    "price": 3000
}

print(type(myBook))

print(myBook)
print(myBook['title'])

myBook['author'] = "Mike"
myBook['price'] = 2000
print(myBook)

del myBook['description']
print(myBook)