person = {"name": "Jame", "age": 21, "gender": "male"}
print(person)

person.setdefault('address', 'No-123, Bla bal Road')
print(person)

print(person.get('driving_license', 'Not Found'))

person.update(name = 'John')
person.update(address = 'London')
print(person)

person.pop('age')
print(person)

person.popitem() #remove last element
print(person)

person2 = person.copy()
person2['job'] = {'dep': "ICT", 'role': "Manager"}

print(person2)
print(person2['job']['dep'])