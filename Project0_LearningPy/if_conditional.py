# If / else conditions are used to decide to do something based on conditions being true or false!
x = 10
y = 5

#--------------------------------------------------------
# Comparison Operators (==, !=, >, <, >=, <=) - used to compare values


#simple if ----------------------
if x > y:
    print(f'{x} is greater than {y}')
    
#10 is greater than 5

#if / else   ---------------------
if x > y:
    print(f'{x} is greater than {y}') 
else:
    print(f'{y} is greater than {x}')  

# 10 is greater than 5
#time: 00:51:55 / 00:43:51

#  elif ---------------------------
if x > y:
    print(f'{x} is greater than {y}')
elif x == y:    # elif need a condition!
    print(f'{x} is equal to {y}')
else:
    print(f'{y} is greater than {x}')    

# 10 is greater than 5

#  Nested if ---------------------- using  and is better!
if x > 2 :
    if x <= 10:
        print(f'{x} is between 2 and 10')    

# 10 is between 2 and 10


#--------------------------------------------------------
# Logical operators (and, or, not) - used to combine conditional statements;
# and --------------
if x > 2 and x <= 10:
    print(f'{x} is between 2 and 10')

# 10 is between 2 and 10

#or -----------------
if x > 2 or x <= 10:
    print(f'{x} is greater than 2 or less than or equal to 10')    

#10 is greater than 2 or less than or equal to 10

#not ------------------
if not(x == y):
    print(f'{x} is not equal to {y}') 

# 10 is not equal to 5

#--------------------------------------------------------
#Membership Operators (not, not in) - Membership operators are used 
# to test if a sequence is presented in an object

numbers = [1,2,3,4] 
x1 = 3
if x1 in numbers:
    print(x1 in numbers)       # True

x2 = 10
if x2 in numbers:
    print(x2 in numbers)       # not verified!

if x2 not in numbers:
    print(x2 not in numbers)   # True   

#  Identify operators (is, is not)- compare the objects,
#  not if they are equal, but if they are actually the same object, 
#  with the same memory location.
# 
# is ------------------

if x is y:
    print(x is y)  # not verified!

# is not

if x is not y:
    print(x is not y)   # True


 