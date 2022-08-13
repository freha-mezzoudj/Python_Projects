# A class is like a blueprint for creating objects.
#An object has properties and methods (functions) associated with it.
# Almost everything in python is an object.

# creat a class
class User:
    #constructor  # self = this (in java)
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f' My name is {self.name} and I am {self.age}'       

    def has_birthday(self):
        self.age+=1

# Extend class 
class Customer(User):
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance    
    
    def greeting(self):
        return f' My name is {self.name} and I am {self.age} and my balance is {self.balance}'       
#-----------------------------------------------#     
# Init user object
brad = User('Brad Traversy', 'brad@gmail.com', 37) 
print('OBject1: ', brad, type(brad))       
# OBject1:  <__main__.User object at 0x0000021E58837CA0>
# <class '__main__.User'>

#Init customer object
janet = Customer('Janet Johnson', 'janet@gmail.com', 25)
janet.set_balance(500)
print(janet.greeting())
# My name is Janet Johnson and I am 25 and my balance is 500


# access to propreities (attributs)
print('age of object 1: ', brad.age)

# access to methods()
brad.has_birthday()
print(brad.greeting())

# We can use the mother's methods or over define new ones.