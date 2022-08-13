#Python has functions for creating, reading, updating and deleting files.

#Open a file
myFile1 = open('myfile1.txt', 'w')
#when we save and run --> myfile1.txt is created!

# Get some info
print('Name: ', myFile1.name)
print('Is closed: ', myFile1.closed)
print('Opening mode: ', myFile1.mode)

#Name:  myfile1.txt
#Is closed:  False
#Opening mode:  w

# Write to file
myFile1.write('I love Python and I will learn it well inshAllah and I will use it to earn a good money!')
myFile1.write(' I also love Javascript!')
myFile1.close()

#if we go to myfile.txt:
#I love Python and I will learn it well inshAllah and I will use it to earn a good money!I also love Javascript!

#Append to file
myFile1 = open('myfile1.txt', 'a')
myFile1.write(' I will also try with PHP.') 
myFile1.close()

#Read from file
myFile1 = open('myfile1.txt', 'r+')
text = myFile1.read(100)  # 100 char
print(text)
#I love Python and I will learn it well inshAllah and I will use it to earn a good money! I also love

