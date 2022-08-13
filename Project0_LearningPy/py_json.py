# A JSON is commonly used with data APIs. 
# Here how we can parse JSON into a Python dictionary.

import json

#sample JSON
userJSON = '{"first_name": "Marwa", "last_name":"Bmz", "age": 18}'

#parse to dict (json format --> py dictionary)
user = json.loads(userJSON)

#take just first_name
print(user['first_name'])
#Marwa
print(user)
#{'first_name': 'Marwa', 'last_name': 'Bmz', 'age': 18}
#----------------------------------------------------
#the opposite:
#how to take a dictionary and turn it in json format

car = {'make' : 'Ford', 'model': 'Mustang', 'year': 1970}
carJSON = json.dumps(car)
print(carJSON)
#{"make": "Ford", "model": "Mustang", "year": 1970}