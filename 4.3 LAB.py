#1.1
#Serialization of Python objects using the shelve module
#There is another handy module, called shelve, that is built on top of pickle, and implements a serialization dictionary where objects are pickled and associated with a key. 
#The keys must be ordinary strings, because the underlying database (dbm) requires strings.
#Therefore, you can open your shelved data file and access your pickled objects via the keys the way you do when you access Python dictionaries. This could be more convenient for you when you’re serializing many objects.

#1.2
#Using shelve is quite easy and intuitive.
#First, let's import the appropriate module and create an object representing a file-based database:

import shelve
my_shelve = shelve.open('first_shelve.shlv', flag='w')

#The meaning of the optional flag parameter:

#Value	Meaning
#'r'	Open existing database for reading only
#'w'	Open existing database for reading and writing
#'c'	Open database for reading and writing, creating it if it doesn’t exist (this is a default value)
#'n'	Always create a new, empty database, open for reading and writing

import shelve

shelve_name = 'first_shelve.shlv'

my_shelve = shelve.open(shelve_name, flag='c')
my_shelve['EUR'] = {'code':'Euro', 'symbol': '€'}
my_shelve['GBP'] = {'code':'Pounds sterling', 'symbol': '£'}
my_shelve['USD'] = {'code':'US dollar', 'symbol': '$'}
my_shelve['JPY'] = {'code':'Japanese yen', 'symbol': '¥'}
my_shelve.close()
#open the shelve file to demonstrate direct access to the elements
new_shelve = shelve.open(shelve_name)
print(new_shelve['USD'])
print(new_shelve['JPY'])
new_shelve.close()
>>
{'code': 'US dollar', 'symbol': '$'}
{'code': 'Japanese yen', 'symbol': '¥'}

#1.3
#You should treat a shelve object as a Python dictionary, with a few additional notes:
#the keys must be strings;
#Python puts the changes in a buffer which is periodically flushed to the disk. To enforce an immediate flush, call the sync() method on your shelve object;
#when you call the close() method on an shelve object, it also flushes the buffers.

#When you treat a shelve object like a Python dictionary, you can make use of the dictionary utilities:

#the len() function;
#the in operator;
#the keys() anditems() methods;
#the update operation, which works the same as when applied to a Python dictionary;
#the del instruction, used to delete a key-value pair.
