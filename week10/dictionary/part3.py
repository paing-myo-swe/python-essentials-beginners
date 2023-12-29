person = {"name": "Jame", "age": 21, "gender": "male"}

print(person)
print(person.keys())
print(person.values())
print(person.get('name'))

for key in person.keys():
    print(key)

for value in person.values():
    print(value)

print(person.items())

for key, value in person.items():
    print(key, ":", value)

person2 = person.fromkeys(person, 1)
print(person2)

person3 = person.copy()
person3['name'] = "Bob"
print(person3)

person2.clear()
print(person2)

