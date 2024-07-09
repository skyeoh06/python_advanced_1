#1.2
#what is a class?
class Duck:
    def __init__(self, height, weight, sex):
        self.height = height
        self.weight = weight
        self.sex = sex

    def walk(self):
        pass

    def quack(self):
        return print('Quack')

#1.3
#what is an instance, what is an object?
#An instance is one particular physical instantiation of a class that occupies memory and has data elements. This is what 'self' refers to when we deal with class instances.
#An object is everything in Python that you can operate on, like a class, instance, list, or dictionary.
#The term instance is very often used interchangeably with the term object, because object refers to a particular instance of a class. It’s a bit of a simplification, because the term object is more general than instance.
#Each instance has its own, individual state (expressed as variables, so objects again) and shares its behavior (expressed as methods, so objects again).
class Duck:
    def __init__(self, height, weight, sex):
        self.height = height
        self.weight = weight
        self.sex = sex

    def walk(self):
        pass

    def quack(self):
        return print('Quack')

duckling = Duck(height=10, weight=3.4, sex="male")
drake = Duck(height=25, weight=3.7, sex="male")
hen = Duck(height=20, weight=3.4, sex="female")
print(duckling)
>> <__main__.Duck object at 0x7f9d7ba085d0>

#1.4
#what is an attribute, what is a method?
#An attribute is a capacious term that can refer to two major kinds of class traits:

#variables, containing information about the class itself or a class instance; classes and class instances can own many variables;
#methods, formulated as Python functions; they represent a behavior that could be applied to the object.
#Each Python object has its own individual set of attributes. We can extend that set by adding new attributes to existing objects, change (reassign) them or control access to those attributes.
#It is said that methods are the 'callable attributes' of Python objects. By 'callable' we should understand anything that can be called; such objects allow you to use round parentheses () and eventually pass some parameters, just like functions.
#This is a very important fact to remember: methods are called on behalf of an object and are usually executed on object data.
#Class attributes are most often addressed with 'dot' notation, i.e., <class>dot<attribute>. The other way to access attributes (variables) it to use the getattr() and setattr() functions.
class Duck:
    def __init__(self, height, weight, sex):
        self.height = height
        self.weight = weight
        self.sex = sex

    def walk(self):
        pass

    def quack(self):
        return print('Quack')

duckling = Duck(height=10, weight=3.4, sex="male")
drake = Duck(height=25, weight=3.7, sex="male")
hen = Duck(height=20, weight=3.4, sex="female")

drake.quack()
print(duckling.height)
print(hen.sex)
print(drake.weight)
>>
Quack
10
female
3.7

#1.5
#what is a type?
#A type is one of the most fundamental and abstract terms of Python:

#it is the foremost type that any class can be inherited from;
#as a result, if you’re looking for the type of class, then type is returned;
#in all other cases, it refers to the class that was used to instantiate the object; it’s a general term describing the type/kind of any object;
#it’s the name of a very handy Python function that returns the class information about the objects passed as arguments to that function;
#it returns a new type object when type() is called with three arguments; we'll talk about this in the 'metaclass' section.
#Information about an object’s class is contained in __class__.
class Duck:
    def __init__(self, height, weight, sex):
        self.height = height
        self.weight = weight
        self.sex = sex

    def walk(self):
        pass

    def quack(self):
        return print('Quack')

duckling = Duck(height=10, weight=3.4, sex="male")
drake = Duck(height=25, weight=3.7, sex="male")
hen = Duck(height=20, weight=3.4, sex="female")

print(Duck.__class__)
print(duckling.__class__)
print(duckling.sex.__class__)
print(duckling.quack.__class__)
>>
<class 'type'>
<class '__main__.Duck'>
<class 'str'>
<class 'method'>

#the Duck class is of the 'type' type;
#the duckling object is an instance type built on the basis of the Duck class, and residing in the __main__ scope;
#the duckling.sex is an attribute of the 'str' type;
#duckling.quack is an attribute of the 'method' type.


