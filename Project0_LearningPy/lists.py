#Alist is a collection which is ordred and chageable. 
# It allows duplicate member.

#Create list: common way
numbers = [1,2,3,4]
print(numbers)
#[1, 2, 3, 4]

#use a constructeur
numbers2 = list((1,2,3,4))
print(numbers2)
#[1, 2, 3, 4]

#Create list of fruits: common way
fruits = ['Appels','Oranges', 'Grapes','Pears']
print(fruits)
#['Appels', 'Oranges', 'Grapes', 'Pears']

print('0:' + fruits[0])            #print a value from the list
print('1:' + fruits[1])
print('2:' + fruits[2])
print('3:' + fruits[3])
# 0:Appels
# 1:Oranges
# 2:Grapes
# 3:Pears

print(len(fruits))                 #the lenght of the list
# 4

fruits.append('Mangos')            #add an element to the list
print(fruits)
# ['Appels', 'Oranges', 'Grapes', 'Pears', 'Mangos']

fruits.remove('Grapes')            #remove an element from the list 
print(fruits)
# ['Appels', 'Oranges', 'Pears', 'Mangos']

fruits.insert(3, 'Strawberries')   #add an element in a position
print(fruits)
# ['Appels', 'Oranges', 'Pears', 'Strawberries', 'Mangos']

fruits.pop(3)                      #remove an elemnt in a position
print(fruits)
# ['Appels', 'Orages', 'Pears', 'Mangos']

fruits.reverse()                   #reverse the current order
print(fruits)
# ['Mangos', 'Pears', 'Orages', 'Appels']

fruits.sort()                      #sort by alphabetic order
print(fruits)
# ['Appels', 'Mangos', 'Orages', 'Pears']

ages = [40, 15, 30, 17, 25] 
print("Before-sort: ", ages)
ages.sort()
print("After-sort: ", ages) 
# Before-sort:  [40, 15, 30, 17, 25]
# After-sort:  [15, 17, 25, 30, 40]

bools =[True, False, True]
bools.sort()
print(bools)
#[False,True,True]

fruits.sort(reverse=True)          # inverse sort alphab-
print(fruits)
# ['Pears', 'Orages', 'Mangos', 'Appels']

# to change a value : affectation 
fruits[0] = 'Blueberries'
print(fruits)
# ['Blueberries', 'Orages', 'Mangos', 'Appels']

#time: 00:23:27 / 01:12:19

