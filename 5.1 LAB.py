#1.2
#Metaprogramming – metaclasses
#In Python, a metaclass is a class whose instances are classes. Just as an ordinary class defines the behavior of certain objects, a metaclass allows for the customization of class instantiation.
#The functionality of the metaclass partly coincides with that of class decorators, but metaclasses act in a different way than decorators:

#decorators bind the names of decorated functions or classes to new callable objects. Class decorators are applied when classes are instantiated;
#metaclasses redirect class instantiations to dedicated logic, contained in metaclasses. Metaclasses are applied when class definitions are read to create classes, well before classes are instantiated.
#Metaclasses usually enter the game when we program advanced modules or frameworks, where a lot of precise automation must be provided.

#The typical use cases for metaclasses:

#logging;
#registering classes at creation time;
#interface checking;
#automatically adding new methods;
#automatically adding new variables.

#1.3
#Metaprogramming – what type is a class?
#In Python's approach, everything is an object, and every object has some type associated with it. To get the type of any object, make use of the type() function.
class Dog:
    pass


age = 10
codes = [33, 92]
dog = Dog()

print(type(age))
print(type(codes))
print(type(dog))
print(type(Dog))
>>
<class 'int'>
<class 'list'>
<class '__main__.Dog'>
<class 'type'>

#The example also shows that we can create our own classes, and those classes will be instances of the type special class, which is the default metaclass responsible for creating classes.
#what type of objects are built-in classes and the metaclass type?
for t in (int, list, type):
    print(type(t))

>>
<class 'type'>
<class 'type'>
<class 'type'>

#These observations lead us to the following conclusions:

#metaclasses are used to create classes;
#classes are used to create objects;
#the type of the metaclass type is type – no, that is not a typo.
#class object is an instance of object is an instance of metaclass.

#To extend the above observations, it’s important to add:

#type is a class that generates classes defined by a programmer;
#metaclasses are subclasses of the type class.
#Before we start creating our own metaclasses, it’s important to understand some more details regarding classes and the process of creating them.

#1.4
#Metaprogramming – special attributes: __name__, __class__, __bases__, and __dict__
#We should get familiar with some special attributes:

#__name__ – inherent for classes; contains the name of the class;
#__class__ – inherent for both classes and instances; contains information about the class to which a class instance belongs;
#__bases__ – inherent for classes; it’s a tuple and contains information about the base classes of a class;
#__dict__ – inherent for both classes and instances; contains a dictionary (or other type mapping object) of the object's attributes.
class Dog:
    pass

dog = Dog()
print('"dog" is an object of class named:', Dog.__name__)
>> "dog" is an object of class named: Dog
print('class "Dog" is an instance of:', Dog.__class__)
>> class "Dog" is an instance of: <class 'type'>
print('instance "dog" is an instance of:', dog.__class__)
>> instance "dog" is an instance of: <class '__main__.Dog'>
print('class "Dog" is  ', Dog.__bases__)
>> class "Dog" is   (<class 'object'>,)
print('class "Dog" attributes:', Dog.__dict__)
>> class "Dog" attributes: {'__module__': '__main__', '__dict__': <attribute '__dict__' of 'Dog' objects>, '__weakref__': <attribute '__weakref__' of 'Dog' objects>, '__doc__': None}
object "dog" attributes: {}
print('object "dog" attributes:', dog.__dict__)
>> object "dog" attributes: {}

#1.5
#The same information stored in __class__could be retrieved by calling a type() function with one argument:
for element in (1, 'a', True):
    print(element, 'is', element.__class__, type(element))
>>
1 is <class 'int'> <class 'int'>
a is <class 'str'> <class 'str'>
True is <class 'bool'> <class 'bool'>

#1.6
#When the type() function is called with three arguments, then it dynamically creates a new class.

#For the invocation of type(, , ):

#the argument specifies the class name; this value becomes the __name__ attribute of the class;
#the argument specifies a tuple of the base classes from which the newly created class is inherited; this argument becomes the __bases__ attribute of the class;
#the argument specifies a dictionary containing method definitions and variables for the class body; the elements of this argument become the __dict__ attribute of the class and state the class namespace.
#A very simple example, when both bases and dictionary are empty
Dog = type('Dog', (), {})

print('The class name is:', Dog.__name__)
print('The class is an instance of:', Dog.__class__)
print('The class is based on:', Dog.__bases__)
print('The class attributes are:', Dog.__dict__)
>>
The class name is: Dog
The class is an instance of: <class 'type'>
The class is based on: (<class 'object'>,)
The class attributes are: {'__module__': '__main__', '__dict__': <attribute '__dict__' of 'Dog' objects>, '__weakref__': <attribute '__weakref__' of 'Dog' objects>, '__doc__': None}

#As a result, we have created the simple class “Dog”.

#1.7
def bark(self):
    print('Woof, woof')

class Animal:
    def feed(self):
        print('It is feeding time!')

Dog = type('Dog', (Animal, ), {'age':0, 'bark':bark})

print('The class name is:', Dog.__name__)
print('The class is an instance of:', Dog.__class__)
print('The class is based on:', Dog.__bases__)
print('The class attributes are:', Dog.__dict__)

doggy = Dog()
doggy.feed()
doggy.bark()
>>
The class name is: Dog
The class is an instance of: <class 'type'>
The class is based on: (<class '__main__.Animal'>,)
The class attributes are: {'age': 0, 'bark': <function bark at 0x7f4a741f60e0>, '__module__': '__main__', '__doc__': None}
It is feeding time!
Woof, woof

#This way of creating classes, using the type function, is substantial for Python's way of creating classes using the class instruction:
#after the class instruction has been identified and the class body has been executed, the class = type(, , ) code is executed;
#the type is responsible for calling the __call__ method upon class instance creation; this method calls two other methods:
#__new__(), responsible for creating the class instance in the computer memory; this method is run before __init__();
#__init__(), responsible for object initialization.
#Metaclasses usually implement these two methods (__init__, __new__), taking control of the procedure of creating and initializing a new class instance. Classes receive a new layer of logic.

#1.8
#It’s important to remember that metaclasses are classes that are instantiated to get classes.
#The first step is to define a metaclass that derives from the type type and arms the class with a 'custom_attribute', as follows:
class My_Meta(type):
    def __new__(mcs, name, bases, dictionary):
        obj = super().__new__(mcs, name, bases, dictionary)
        obj.custom_attribute = 'Added by My_Meta'
        return obj

#the class My_Meta is derived from type. This makes our class a metaclass;
#our own __new__ method has been defined. Its role is to call the __new__ method of the parent class to create a new class;
#__new__ uses 'mcs' to refer to the class – it’s just a convention;
#a class attribute is created additionally;
#the class is returned.
#use of the metaclass to create our own, domain-specific class,
class My_Object(metaclass=My_Meta):
    pass

print(My_Object.__dict__)
>> {'__module__': '__main__', '__dict__': <attribute '__dict__' of 'My_Object' objects>, '__weakref__': <attribute '__weakref__' of 'My_Object' objects>, '__doc__': None, 'custom_attribute': 'Added by My_Meta'}
#a new class has been defined in a way where a custom metaclass is listed in the class definition as a metaclass. This is a way to tell Python to use My_Meta as a metaclass, not as an ordinary superclass;
#we are printing the contents of the class __dict__ attribute to check if the custom attribute is present.

#1.9
#Metaprogramming – another metaclass
#In My_Class1, by design, there is no greetings function, so when the class is constructed, it is equipped with a default function by the metaclass.
#In contrast, in My_Class2 the greetings function is present from the very beginning.
#Both classes rely on the same metaclass.
def greetings(self):
    print('Just a greeting function, but it could be something more serious like a check sum')

class My_Meta(type):
    def __new__(mcs, name, bases, dictionary):
        if 'greetings' not in dictionary:
            dictionary['greetings'] = greetings
        obj = super().__new__(mcs, name, bases, dictionary)
        return obj

class My_Class1(metaclass=My_Meta):
    pass

class My_Class2(metaclass=My_Meta):
    def greetings(self):
        print('We are ready to greet you!')

myobj1 = My_Class1()
myobj1.greetings()
myobj2 = My_Class2()
myobj2.greetings()
>>
Just a greeting function, but it could be something more serious like a check sum
We are ready to greet you!

#This is how metaclasses become very useful – they can control the process of class instantiation, and adjust created classes to conform with selected rules.



