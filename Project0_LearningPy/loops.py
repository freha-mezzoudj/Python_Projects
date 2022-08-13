# A for loop is used for iterating over a sequence 
# (that is either a list, a tuple, a dictionary, a set or a string)

people=['Hind', 'Anes', 'Marwa', 'Mouad']

# Simple for loop-----------
for person in people:
    print(f'Current person: {person}')

#Current person: Hind
#Current person: Anes
#Current person: Marwa
#Current person: Mouad

#Break ----------------------
print('for loop with break:')
for person in people:
    if person == 'Marwa':
        break                      # stop loop if the personn is Marwa
    print(f'Current person: {person}')

#Current person: Hind
#Current person: Anes


#continue ----------------------
print('for loop with continue:')
for person in people:
    if person == 'Marwa':
        continue                      # skip the person Marwa and continue the loop. 
    print(f'Current person: {person}')

#Current person: Hind
#Current person: Anes
#Current person: Mouad

#range -------------------------
for i in range(len(people)):
    print(people[i])

#Hind
#Anes
#Marwa
#Mouad    


for i in range(0, 11):
    print(f'Number {i}')

# Number 0
# Number 1
# Number 2
# Number 3
# Number 4
# Number 5
# Number 6
# Number 7
# Number 8
# Number 9
# Number 10  

  

#*******************************************************************#
# While loops execute a set of statements as long as a condition is true

i = 0
while i <= 10:
    print(f'i: {i}')
    i+=1

# i: 0
# i: 1
# i: 2
# i: 3 
# i: 4
# i: 5
# i: 6
# i: 7
# i: 8
# i: 9
# i: 10
    


