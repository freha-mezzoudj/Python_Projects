# A function is a block of code which only runs when it is called. 
# In Python, we do not use curly brakets, we use indentation with tabs or spaces.

#Create function 
def sayHello(name):
    print(f'Hello {name}')    
# Hello Marwa Bmz

sayHello('Marwa Bmz')
# sayHello()      # gives error

#Create function with a default parameter
def sayHelloDef(name = 'Khoia'):
    print(f'Hello {name}')

sayHelloDef('Marwa')
# Hello Marwa

sayHelloDef()  # without paramter   
# Hello Khoia
# 
# Return values
def getSum(num1, num2):
    total = num1 + num2
    return total

#Use a function 'return'
num = getSum(7,5)   
print(num)                     # 12

# or directly
print(getSum(4,6))             # 10
print(getSum('hi, ', 'Marwa')) # hi, Marwa



# ***********************************************#
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, 
# but can only have one expression.
# Very similar to JS arrow function.

getSumLmd = lambda num1, num2 : num1 + num2 
print(getSumLmd(10, 3))   
# 13
print(getSumLmd('hello', ' world'))
# hello world

#print(getSumLmd(4,5,6))   # error!