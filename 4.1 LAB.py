#1.3
#What is that object 'identity'? Why are the object value and label not enough?
#The built-in id() function returns the 'identity' of an object. This is an integer which is guaranteed to be unique and constant for this object during its lifetime. Two objects with non-overlapping lifetimes may have the same id() value.
a_string = '10 days to departure'
b_string = '20 days to departure'

print('a_string identity:', id(a_string))
print('b_string identity:', id(b_string))
>>
a_string identity: 139728100495808
b_string identity: 139728100495888

#CPython implementation detail: This is the address of the object in the memory. Don’t treat it as an absolute memory address.
#This function is rarely used in applications. More often you’ll use it to debug the code or to experiment while copying objects.
#The side effect of this infrequent use is that some developers forget about its existence and create their own variables titled id to store some kind of identity or identifier.
#As a result, a variable called id shadows the genuine function and makes it unreachable in the scope in which the variable has been defined. You should remember to avoid such situations!

#1.4
#When you have two variables referring to the same object, the return values of the id() function must be the same.
a_string = '10 days to departure'
b_string = a_string

print('a_string identity:', id(a_string))
print('b_string identity:', id(b_string))
>>
a_string identity: 140309848949184
b_string identity: 140309848949184

#1.5
#What is the difference between the '==' and 'is' operators?
#In order to compare two objects, you should start with the '==' operator as usual. This operator compares the values of both operands and checks for value equality. So here we witness a values comparison.
#In fact, two distinct objects holding the same values could be compared, and the result would be 'True'. Moreover, when you compare two variables referencing the same object, the result would be also 'True'.
#To check whether both operands refer to the same object or not, you should use the 'is' operator. 
a_string = ['10', 'days', 'to', 'departure']
b_string = a_string

print('a_string identity:', id(a_string))
print('b_string identity:', id(b_string))
print('The result of the value comparison:', a_string == b_string)
print('The result of the identity comparison:', a_string is b_string)
>>
a_string identity: 140037050253872
b_string identity: 140037050253872
The result of the value comparison: True
The result of the identity comparison: True

a_string = ['10', 'days', 'to', 'departure']
b_string = ['10', 'days', 'to', 'departure']

print('a_string identity:', id(a_string))
print('b_string identity:', id(b_string))
print('The result of the value comparison:', a_string == b_string)
print('The result of the identity comparison:', a_string is b_string)
>>
a_string identity: 140037050256432
b_string identity: 140037049015024
The result of the value comparison: True
The result of the identity comparison: False

#1.6
#Let's have a look at the following code. Its intention is to:
#make a real, independent copy of a_list, (not just a copy reference). Using [:], which is an array slice syntax, we get a fresh copy of the a_list object;
#modify the original object;
#see the contents of both objects.
print("Part 1")
print("Let's make a copy")
a_list = [10, "banana", [997, 123]]
b_list = a_list[:]
print("a_list contents:", a_list)
print("b_list contents:", b_list)
print("Is it the same object?", a_list is b_list)
>>
Part 1
Let's make a copy
a_list contents: [10, 'banana', [997, 123]]
b_list contents: [10, 'banana', [997, 123]]
Is it the same object? False

print("Part 2")
print("Let's modify b_list[2]")
b_list[2][0] = 112
print("a_list contents:", a_list)
print("b_list contents:", b_list)
print("Is it the same object?", a_list is b_list)
>>
Part 2
Let's modify b_list[2]
a_list contents: [10, 'banana', [112, 123]]
b_list contents: [10, 'banana', [112, 123]]
Is it the same object? False

#So, despite the fact that b_list is a copy of a_list, modifying b_list results in a modification of the a_list object.
#The explanation of the behavior:
#the 'a_list' object is a compound object;
#we’ve run a shallow copy that constructs a new compound object, b_list in our example, and then populated it with references to the objects found in the original;
#a shallow copy is only one level deep. The copying process does not recurse and therefore does not create copies of the child objects, but instead populates b_list with references to the already existing objects.

#1.8
#If you want to make an independent copy of a compound object (list, dictionary, custom class instance) you should make use of deep copy, which:
#constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original;
#takes more time to complete, as there are many more operations to be performed;
#is implemented by the deepcopy() function, delivered by the python 'copy' module
import copy

print("Let's make a deep copy")
a_list = [10, "banana", [997, 123]]
b_list = copy.deepcopy(a_list)
print("a_list contents:", a_list)
print("b_list contents:", b_list)
print("Is it the same object?", a_list is b_list)
>>
Let's make a deep copy
a_list contents: [10, 'banana', [997, 123]]
b_list contents: [10, 'banana', [997, 123]]
Is it the same object? False

print("Let's modify b_list[2]")
b_list[2][0] = 112
print("a_list contents:", a_list)
print("b_list contents:", b_list)
print("Is it the same object?", a_list is b_list)
>>
Let's modify b_list[2]
a_list contents: [10, 'banana', [997, 123]]
b_list contents: [10, 'banana', [112, 123]]
Is it the same object? False

#The 'copy' module contains a function for shallow copying: copy(). 
#But think about making use of polymorphism when you need a universal function to copy any type object, so that in that case using a copy() function is the smart way to accomplish the task.

#1.9
#In the following example, we'll compare the performance of three ways of copying a large compound object (a million three-element tuples).
#The first approach is a simple reference copy. This is done very quickly, as there’s nearly nothing to be done by the CPU – just a copy of a reference to 'a_list'.
import copy
import time

a_list = [(1,2,3) for x in range(1_000_000)]

print('Single reference copy')
time_start = time.time()
b_list = a_list
print('Execution time:', round(time.time() - time_start, 3))
print('Memory chunks:', id(a_list), id(b_list))
print('Same memory chunk?', a_list is b_list)
>>
Single reference copy
Execution time: 0.0
Memory chunks: 139934856848160 139934856848160
Same memory chunk? True

#The second approach is a shallow copy. This is slower than the previous code, as there are 1,000,000 references (not objects) created.
print('Shallow copy')
time_start = time.time()
b_list = a_list[:]
print('Execution time:', round(time.time() - time_start, 3))
print('Memory chunks:', id(a_list), id(b_list))
print('Same memory chunk?', a_list is b_list)
>>
SShallow copy
Execution time: 0.02
Memory chunks: 139934856848160 139934856524656
Same memory chunk? False

#The third approach is a deep copy. This is the most comprehensive operation, as there are 3,000,000 objects created.
print('Deep copy')
time_start = time.time()
b_list = copy.deepcopy(a_list)
print('Execution time:', round(time.time() - time_start, 3))
print('Memory chunks:', id(a_list), id(b_list))
print('Same memory chunk?', a_list is b_list)
>>
Deep copy
Single reference copy
Execution time: 0.0
Memory chunks: 139840077320912 139840077320912
Same memory chunk? True

#1.10
#The same deepcopy() method could be utilized when you want to copy dictionaries or custom class objects.
import copy

a_dict = {
    'first name': 'James',
    'last name': 'Bond',
    'movies': ['Goldfinger (1965)', 'You Only Live Twice']
    }
b_dict = copy.deepcopy(a_dict)
print('Memory chunks:', id(a_dict), id(b_dict))
print('Same memory chunk?', a_dict is b_dict)
print("Let's modify the movies list")
a_dict['movies'].append('Diamonds Are Forever (1971)')
b_dict['movies'][0]='Diamonds Are Forever (1972)'
print('a_dict movies:', a_dict['movies'])
print('b_dict movies:', b_dict['movies'])
>>

Memory chunks: 139994175509920 139994174802912
Same memory chunk? False
Let's modify the movies list
a_dict movies: ['Goldfinger (1965)', 'You Only Live Twice', 'Diamonds Are Forever (1971)']
b_dict movies: ['Diamonds Are Forever (1972)', 'You Only Live Twice']

#1.11
#The code in the editor copies the dictionary in a safe manner.
import copy

class Example:
    def __init__(self):
        self.properties = ["112", "997"]
        print("Hello from __init__()")

a_example = Example()
b_example = copy.deepcopy(a_example)
print("Memory chunks:", id(a_example), id(b_example))
print("Same memory chunk?", a_example is b_example)
print()
print("Let's modify the movies list")
b_example.properties.append("911")
print('a_example.properties:', a_example.properties)
print('b_example.properties:', b_example.properties)
>>
Hello from __init__()
Memory chunks: 140225827267728 140225827267984
Same memory chunk? False

Let's modify the movies list
a_example.properties: ['112', '997']
b_example.properties: ['112', '997', '911']

#Pay attention to the fact that the __init__() method is executed only once, despite the fact we own two instances of the example class.
#This method is not executed for the b_example object as the deepcopy function copies an already initialized object.

#Section summary
#Important things to remember:

#the deepcopy() method creates and persists new instances of source objects, whereas any shallow copy operation only stores references to the original memory address;
#a deep copy operation takes significantly more time than any shallow copy operation;
#the deepcopy() method copies the whole object, including all nested objects; it’s an example of practical recursion taking place;
#deep copy might cause problems when there are cyclic references in the structure to be copied.



