# A module is basically a file containing a set of functions
# to include in your application.
#There are core python modules, modules can be installed using:
#  'pip' package manager.
# modules such as: Django, or your custom modules.
# 2 core modules available in python: datetime & time
import datetime #-------------------
today = datetime.date.today()
print(today)
# 2022-08-13

# if I need to import just "data"
# ------------------------------------------------------
from datetime import date
today1 = date.today   # without datetime (as in line 8)
print(today1)
# 2022-08-13
# <built-in method today of type object at 0x00007FF99B58FBA0>
#-------------------------------------------------------

import time
timestamp = time.time()
print(timestamp)
#1660342416.6956937

# or import only time!
from time import time
timestamp1 = time()
print(timestamp1)
#1660342580.4169397


# installed modules ------------------------

# with python3, pip3 is used to install packages.
# you can use pip in virtual environement 
# instead do it globaly in the system!
#on terminal -->
# python --version: python 3.10.0
# pip3 --version :  pip 21.2.3 
#pip3 freeze     : to see all the packages installed using pip3.




# pip3 install camelcase
#Collecting camelcase
#  Downloading camelcase-0.2.tar.gz (1.3 kB)
#Using legacy 'setup.py install' for camelcase, since package 'wheel' is not installed.
#Installing collected packages: camelcase
#    Running setup.py install for camelcase ... done
#Successfully installed camelcase-0.2

#pip3 freeze
#camelcase==0.2

# import camelcase
from camelcase import CamelCase
c = CamelCase()
print(c.hump('hello there world'))
#Hello There World



# costum module to be imported
import validator
from validator import validate_email

email = 'test@test.com'
if validate_email(email):
    print('Email is correct')
else:
    print('Email is bad')  

# Email is correct


email1 = 'testtest.com' 
if validate_email(email1):
    print('Email is correct')
else:
    print('Email is bad') 

# Email is bad

# time: 01:15:50 / 00:19:56


