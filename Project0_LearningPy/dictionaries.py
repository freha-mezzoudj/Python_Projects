# A dictionary is a collection which is un_ordred, changeble and indexed.
# No duplicate members.

# create dict: key:value
person = {
    'first_name': 'Marwa',
    'last_name' : 'Bmz',
    'age' : 18,
}

print(person, type(person))
# {'first_name': 'Marwa', 'last_name': 'Bmz', 'age': 18}
#  <class 'dict'>

# using a constructor (key = value)
person2 = dict(first_name = 'Mina', last_name = 'Bz', age = 17)
print(person2, type(person2))
#{'first_name': 'Mina', 'last_name': 'Bz', 'age': 17} 
# <class 'dict'>

# Get value:
print(person['first_name'])
print(person.get('first_name'))
# Marwa
# Marwa 

# Get Keys:
print(person.keys())
#dict_keys(['first_name', 'last_name', 'age'])

# Get Items:
print(person.items())
# dict_items([('first_name', 'Marwa'), ('last_name', 'Bmz'), ('age', 18)])
 
#Copy a dictionnary by "copy()"
person3 = person.copy()
print("person: ", person)
print("person3: ", person3)
#person:  {'first_name': 'Marwa', 'last_name': 'Bmz', 'age': 18}
#person3:  {'first_name': 'Marwa', 'last_name': 'Bmz', 'age': 18}

# add item to copy: 
person3['city'] = 'AET'
print("person: ", person)
print("person3: ", person3)
#person:  {'first_name': 'Marwa', 'last_name': 'Bmz', 'age': 18}
#person3:  {'first_name': 'Marwa', 'last_name': 'Bmz', 'age': 18, 'city': 'AET'}

#remove item:(del |  pop):
del(person3['age'])
print("person3-age: ", person3)
person3.pop('city')
print("person3-city: ", person3)
# person3-age:  {'first_name': 'Marwa', 'last_name': 'Bmz', 'city': 'AET'}
# person3-city: {'first_name': 'Marwa', 'last_name': 'Bmz'}



# Add key/value:
print("Before: ", person)
person['phone'] = '555-555-5555'
print("After: ", person)
# Before: {'first_name': 'Marwa', 'last_name': 'Bmz', 'age': 18}
# After:  {'first_name': 'Marwa', 'last_name': 'Bmz', 'age': 18, 'phone': '555-555-5555'}

# Clear dict
print("Before clear: ", person)
person.clear()
print("After claer: ", person)
#Before clear:  {'first_name': 'Marwa', 'last_name': 'Bmz', 'age': 18, 'phone': '555-555-5555'}
#After claer:  {}

#Get length (key/value paires ?)
print(person2, " - Its length: ", len(person2))
#{'first_name': 'Mina', 'last_name': 'Bz', 'age': 17} 
# - Its length:  3

#Create a list of dict (people):
people = [{'name': 'Marwa', 'age':18},
          {'name': 'Mouad', 'age':17}
         ]
print(people, type(people)) 
#[{'name': 'Marwa', 'age': 18}, {'name': 'Mouad', 'age': 17}] 
# <class 'list'>   
# 
# Get a value from list of dict
#how to have 'Marwa' ?
print(people[0]['name']) 
# Marwa    