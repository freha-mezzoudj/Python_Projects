#All about strings
#String in python are surrounded by " " or ' ' marks.
# String formatting
name = 'Marwa'
age = 18
#concatenation
# print('Hello, my name is '+ name + ' and I am ' + age)
# TypeError: can only concatenate str (not "int") to str

print('1: Hello, my name is '+ name + ' and I am ' + str(age)+ ' :)')

#or using arguments by position without casting
print('2: My name is {name} and I am {age} !'.format(name=name, age=age))
print('2: My name is {name} and I am {age} :)'.format(name='Marwa', age=18))

#F-String (3.6+)
print(f'3: Hello, my name is {name} and I am {age} !!') #like: js language

# String Methods
print('String ''s methods: ') 
s = 'hello world'
s1 = 'hello'
s2 ='world'
#capitalize the string: the first letter
print('1: '+ s)                            #str s 
print('2: ' + s.capitalize())              #upper the first letter    
print('2: '+ s1.capitalize()+ ' ' + s2.capitalize())
print('2: '+ s1.capitalize()+ s2.capitalize())

print('3: ' + s.lower())                     #make all lower
print('4: '+ s.upper())                      #make all uppercase
print('5: ' + s.lower())                     #make all lower
print('6: '+ s.swapcase())               #swap case
print('6: '+ s1.swapcase())                #swap case
print(len(s), type(len(s)))                                #length1
print('7: ' + str(len(s)))                   #length2
print('8: '+ s.replace('world', 'everyone')) #replace
print('8: '+ s)
sub = 'o'                                    # my sub str
print('9: ' + str(s.count(sub))+ ' or :')             #count how many 'o'
print(s.count(sub))                          #count how many 'h'
print('10: '+ str(s.startswith('hello')))
print('11: '+ str(s.endswith('world')))
print('12: '+ str(s.split()))                #split into a list 
print('13: '+ str(s.find('r')))              #find position of 'r'
print('14: '+ str(s.isalnum()))              #is all alphanumeric
print('15: '+ str(s.isalpha()))              #is all alphabetic
print('16: '+ str(s.isnumeric()))            #is all numeric
#time: 00:16:14  / 01:19:32
#note : without the space, s1 is alphanumeric and alphabetic (True)
s1 = 'helloworld'
print('17: '+ str(s1.isalnum()))              #is all alphanumeric
print('18: '+ str(s1.isalpha()))              #is all alphabetic
print('19: '+ str(s1.isnumeric()))            #is all numeric




