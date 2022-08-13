# alternative1
x = 4             #int
y = 2.5           #float
y2 = 0            #int
name = 'marwa'    #str
myTown = 'oran'   #str
is_good = True    #bool
print(x, y, name, myTown, is_good)
# 4 2.5 marwa oran True  

# alternative2 (more compact)
x1, y1, name1, town2 =(5, 2.8, 'mina', 'AET')
print(x1, y1, name1, town2)
#5 2.8 mina AET

#basic Math
z = x + x
z1 = x + y
z2 = x * y
#if (y != 0) 
z3 = x/y
# z4 = x/y2
z5 = x % 2

print(z, z1, z2, z3, z5)
#8 6.5 10.0 1.6 0
#types(int, float, str) and casting
print (type(x), type(x1), type(y), type(name), type(is_good)) # int, int
#<class 'int'> <class 'int'> <class 'float'> <class 'str'> <class 'bool'>   

#casting 
x = str(x)
y = int(y)
x1 = float(x1)

print(type(x),type(y), y, type(x1), x1)
#<class 'str'> <class 'int'> 2 <class 'float'> 5.0


