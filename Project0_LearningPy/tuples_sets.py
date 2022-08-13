# A tuple is a collection which is ordered and "unchageable".
# It allows duplicate members.
#create tuple: by affectation or constructor
fruits_tuple = ('Apples', 'Oranges', 'Grapes')
fruits2_tuple = tuple(('Apples', 'Oranges', 'Grapes'))
print (fruits_tuple)
# ('Apples', 'Oranges', 'Grapes')
print(fruits2_tuple)
# ('Apples', 'Oranges', 'Grapes')

fruits3= ('Apples')
print("fruits3 value: ", fruits3, "-type of fruits3: ", type(fruits3))
# fruits3 value:  Apples 
# -type of fruit3:  <class 'str'>

#single value in tuple needs trailing comma:
fruits4_tuple = ('Apples',)
print("fruits4_tuple value: ", fruits4_tuple, "-type of fruits4: ", type(fruits4_tuple))
# fruits4_tuple value:  ('Apples',) 
# -type ]of fruits4_tuple:  <class 'tuple'>


# Get a value from: fruits = ('Apples', 'Oranges', 'Grapes')
print(fruits_tuple[0])
print(fruits_tuple[1])
print(fruits_tuple[2])

# Apples
# Oranges
# Grapes

# Can't change value of a tuple
# fruits_tuple[0] = 'Pears'               // it gives an error!
# print(fruits_tuple[0])

# error: 
# Traceback (most recent call last):
# File "c:\Users\farah\Documents\vs_code_projects\Python_Projects\project0\tuples_sets.py", line 33, in <module>
#    fruits_tuple[0] = 'Pears'
# TypeError: 'tuple' object does not support item assignment

# Delete tuple: we can't change a tuple but we can deleted definitivly!
print(fruits_tuple)
# ('Apples', 'Oranges', 'Grapes')
del fruits_tuple
# print(fruits_tuple)  // it gives an error 

#error:
# Traceback (most recent call last):
#  File "c:\Users\farah\Documents\vs_code_projects\Python_Projects\project0\tuples_sets.py", line 44, in <module>
#    print(fruits_tuple)
#NameError: name 'fruits_tuple' is not defined. Did you mean: 'fruits2'?

# Get a length
fruits5_tuple = ('Apples', 'Oranges', 'Grapes', 'Pears')
print(fruits5_tuple)
# ('Apples', 'Oranges', 'Grapes', 'Pears')
print("lenght : ", len(fruits5_tuple))
# lenght :  4



#-------------------------------------------------------#
#-------------------------------------------------------#
# A set is a collection which is un-ordred and un-indexed. 
# No duplicated members.

# if you are in situation, where you haven't to deplicate elements --> use "sets"

# to create a set, we use { }:
fruits_set = {'Apples', 'Oranges', 'Mangos'}
print (fruits_set, type(fruits_set)) 

# {'Mangos', 'Apples', 'Oranges'} <class 'set'>

# check if elt is in set?
print('Apples' in fruits_set)
# True

# Add to set
fruits_set.add('Grapes')
print(fruits_set)

# {'Grapes', 'Mangos', 'Oranges', 'Apples'}
# or : {'Grapes', 'Apples', 'Oranges', 'Mangos'}
 
# Add duplicate to set  // impossible to add deplicate to set
print("Before: ", fruits_set)
fruits_set.add('Oranges')
print("After: ", fruits_set)
# Before:  {'Oranges', 'Mangos', 'Grapes', 'Apples'}
# After:  {'Oranges', 'Mangos', 'Grapes', 'Apples'}

# Remove from set
fruits_set.remove('Grapes')
print (fruits_set)
# {'Mangos', 'Oranges', 'Apples'}

# Clear set to have an empty set (which exists but it is empty)
fruits_set.clear()
print(fruits_set)
# set()

# Delete set
del fruits_set
# print(fruits_set)    // it gives an error

# error:
# Traceback (most recent call last):
# File "c:\Users\farah\Documents\vs_code_projects\Python_Projects\project0\tuples_sets.py", line 100, in <module>
#    print(fruits_set)
# NameError: name 'fruits_set' is not defined


