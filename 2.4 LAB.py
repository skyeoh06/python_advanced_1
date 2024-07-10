#1.2
#Function decorators
#let's create functions – simple_hello() and simple_bye()
def simple_hello():
    print("Hello from simple function!")
    
def simple_bye():
    print("Hello from bye function!")

#Let's create another function, simple_decorator(), which is more interesting as it accepts an object as a parameter, displays a __name__ attribute value of the parameter, and returns an accepted object.
def simple_decorator(function):
    print('We are about to call "{}"'.format(function.__name__))
    return function

#The last lines are responsible for both method invocations:

decorated = simple_decorator(simple_hello)
decoratedB = simple_decorator(simple_bye)
decorated()
decoratedB()
>>
We are about to call "simple_hello"
We are about to call "simple_bye"
Hello from simple function!
Hello from bye function!

#1.3
#We have created a simple decorator – a function which accepts another function as its only argument, prints some details, and returns a function or other callable object.
#the definition of the simple_hello() function and simple_bye() functionis literally decorated with '@simple_decorator'.
def simple_decorator(function):
    print('We are about to call "{}"'.format(function.__name__))
    return function


@simple_decorator
def simple_hello():
    print("Hello from simple function!")

@simple_decorator
def simple_bye():
    print("Bye from simple function!")


simple_hello()
simple_bye()
>>
We are about to call "simple_hello"
We are about to call "simple_bye"
Hello from simple function!
Bye from simple function!

#This means that:
#operations are performed on object names;
#this is the most important thing to remember: the name of the simple_function object ceases to indicate the object representing our simple_function() and 
#from that moment on it indicates the object returned by the decorator, the simple_decorator.

#1.4
#Decorators should be universal
#Decorators, which should be universal, must support any function, regardless of the number and type of arguments passed. In such a situation, we can use the *args and **kwargs concepts. 
#We can also employ a closure technique to persist arguments.
#The code presented shows how the decorator can handle the arguments of the function being decorated.
def simple_decorator(own_function):

    def internal_wrapper(*args, **kwargs):
        print('"{}" was called with the following arguments'.format(own_function.__name__))
        print('\t{}\n\t{}\n'.format(args, kwargs))
        own_function(*args, **kwargs)
        print('Decorator is still operating')

    return internal_wrapper


@simple_decorator
def combiner(*args, **kwargs):
    print("\tHello from the decorated function; received arguments:", args, kwargs)

combiner('test',' resst', exec='yes')
>>
"combiner" was called with the following arguments
	('test', ' resst')
	{'exec': 'yes'}

	Hello from the decorated function; received arguments: ('test', ' resst') {'exec': 'yes'}
Decorator is still operating

#Arguments passed to the decorated function are available to the decorator, so the decorator can print them. This is a simple example, as the arguments were just printed, but not processed further.
#A nested function (internal_wrapper) could reference an object (own_function) in its enclosing scope thanks to the closure.


#1.5
#Decorators can accept their own attributes
#The warehouse_decorator() function created in this way has become much more flexible and universal than 'simple_decorator', because it can handle different materials.
#The pack_books function will be executed as follows:

#the warehouse_decorator('kraft') function will return the wrapper function;
#the returned wrapper function will take the function it is supposed to decorate as an argument;
#the wrapper function will return the internal_wrapper function, which adds new functionality (material display) and runs the decorated function.
#The biggest advantage of decorators is now clearly visible:

#we don’t have to change every 'pack' function to display the material being used;
#we just have to add a simple one liner in front of each function definition.
def warehouse_decorator(material):
    def wrapper(our_function):
        def internal_wrapper(*args):
            print('<strong>*</strong> Wrapping items from {} with {}'.format(our_function.__name__, material))
            our_function(*args)
            print()
        return internal_wrapper
    return wrapper


@warehouse_decorator('kraft')
def pack_books(*args):
    print("We'll pack books:", args)


@warehouse_decorator('foil')
def pack_toys(*args):
    print("We'll pack toys:", args)


@warehouse_decorator('cardboard')
def pack_fruits(*args):
    print("We'll pack fruits:", args)


pack_fruits('plum', 'pear')
pack_books('Alice in Wonderland', 'Winnie the Pooh')
pack_toys('doll', 'car')
>>
<strong>*</strong> Wrapping items from pack_fruits with cardboard
We'll pack fruits: ('plum', 'pear')

<strong>*</strong> Wrapping items from pack_books with kraft
We'll pack books: ('Alice in Wonderland', 'Winnie the Pooh')

<strong>*</strong> Wrapping items from pack_toys with foil
We'll pack toys: ('doll', 'car')

#1.6
#Decorator stacking
#Python allows you to apply multiple decorators to a callable object (function, method or class).
#The most important thing to remember is the order in which the decorators are listed in your code, because it determines the order of the executed decorators. 
#When your function is decorated with multiple decorators:

@outer_decorator
@inner_decorator
def function():
    pass

abcd = subject_matter_function()

#the call sequence will look like the following:
#the outer_decorator is called to call the inner_decorator, then the inner_decorator calls your function;
#when your function ends it execution, the inner_decorator takes over control, and after it finishes its execution, the outer_decorator is able to finish its job.
#This routing mimics the classic stack concept.
#The syntactic sugar presented above is the equivalent of the following nested calls:

subject_matter_function = outer_decorator(inner_decorator(subject_matter_function())))
abcd = subject_matter_function()
#Another advantage becomes clear when you think about the number of modifications you should add to gain the same functionality, because you'd have to modify each call to your function.

def big_container(collective_material):
    def wrapper(our_function):
        def internal_wrapper(*args):
            our_function(*args)
            print('<strong>*</strong> The whole order would be packed with', collective_material)
            print()
        return internal_wrapper
    return wrapper

def warehouse_decorator(material):
    def wrapper(our_function):
        def internal_wrapper(*args):
            our_function(*args)
            print('<strong>*</strong> Wrapping items from {} with {}'.format(our_function.__name__, material))
        return internal_wrapper
    return wrapper

@big_container('plain cardboard')
@warehouse_decorator('bubble foil')
def pack_books(*args):
    print("We'll pack books:", args)

@big_container('colourful cardboard')
@warehouse_decorator('foil')
def pack_toys(*args):
    print("We'll pack toys:", args)

@big_container('strong cardboard')
@warehouse_decorator('cardboard')
def pack_fruits(*args):
    print("We'll pack fruits:", args)


pack_books('Alice in Wonderland', 'Winnie the Pooh')
pack_toys('doll', 'car')
pack_fruits('plum', 'pear')
>>
We'll pack books: ('Alice in Wonderland', 'Winnie the Pooh')
<strong>*</strong> Wrapping items from pack_books with bubble foil
<strong>*</strong> The whole order would be packed with plain cardboard

We'll pack toys: ('doll', 'car')
<strong>*</strong> Wrapping items from pack_toys with foil
<strong>*</strong> The whole order would be packed with colourful cardboard

We'll pack fruits: ('plum', 'pear')
<strong>*</strong> Wrapping items from pack_fruits with cardboard
<strong>*</strong> The whole order would be packed with strong cardboard

#We’ve created two decorators:

#big_container – which packs boxes into the collective material passed
#warehouse_decorator – which wraps single items into different materials.
#We’ve also created functions for packaging different kinds of items, each decorated with two decorators.
#This example demonstrates that packaging functions are called simply (and could be called many times in different places in your code) 
#and every time those functions' behavior would be extended in a relevant way.

#1.8
#Decorating functions with classes
#A decorator does not have to be a function. In Python, it could be a class that plays the role of a decorator as a function.

#We can define a decorator as a class, and in order to do that, we have to use a __call__ special class method. When a user needs to create an object that acts as a function (i.e., it is callable) then the function decorator needs to return an object that is callable, 
#so the __call__ special method will be very useful.
class SimpleDecorator:
    def __init__(self, own_function):
        self.func = own_function

    def __call__(self, *args, **kwargs):
        print('"{}" was called with the following arguments'.format(self.func.__name__))
        print('\t{}\n\t{}\n'.format(args, kwargs))
        self.func(*args, **kwargs)
        print('Decorator is still operating')


@SimpleDecorator
def combiner(*args, **kwargs):
    print("\tHello from the decorated function; received arguments:", args, kwargs)


combiner('a', 'b', exec='yes')
>>
"combiner" was called with the following arguments
	('a', 'b')
	{'exec': 'yes'}

	Hello from the decorated function; received arguments: ('a', 'b') {'exec': 'yes'}
Decorator is still operating

#A short explanation of special methods:

#the __init__ method assigns a decorated function reference to the self.attribute for later use;
#the __call__ method, which is responsible for supporting a case when an object is called, calls a previously referenced function.
#The advantage of this approach, when compared to decorators expressed with functions, is:

#classes bring all the subsidiarity they can offer, like inheritance and the ability to create dedicated supportive methods.

#1.9
#Decorators with arguments
class WarehouseDecorator:
    def __init__(self, material):
        self.material = material

    def __call__(self, own_function):
        def internal_wrapper(*args, **kwargs):
            print('<strong>*</strong> Wrapping items from {} with {}'.format(own_function.__name__, self.material))
            own_function(*args, **kwargs)
            print()
        return internal_wrapper


@WarehouseDecorator('kraft')
def pack_books(*args):
    print("We'll pack books:", args)


@WarehouseDecorator('foil')
def pack_toys(*args):
    print("We'll pack toys:", args)


@WarehouseDecorator('cardboard')
def pack_fruits(*args):
    print("We'll pack fruits:", args)


pack_books('Alice in Wonderland', 'Winnie the Pooh')
pack_toys('doll', 'car')
pack_fruits('plum', 'pear')
>>
<strong>*</strong> Wrapping items from pack_books with kraft
We'll pack books: ('Alice in Wonderland', 'Winnie the Pooh')

<strong>*</strong> Wrapping items from pack_toys with foil
We'll pack toys: ('doll', 'car')

<strong>*</strong> Wrapping items from pack_fruits with cardboard
We'll pack fruits: ('plum', 'pear')

#When you pass arguments to the decorator, the decorator mechanism behaves quite differently than presented in example of decorator that does not accept arguments (previous slide):

#the reference to function to be decorated is passed to __call__ method which is called only once during decoration process,
#the decorator arguments are passed to __init__ method


#1.10
#Class decorators
#The simplest use can be presented as follows:

@my_decorator
class MyClass:

obj = MyClass()

#and it is adequate for the following snippet:

def my_decorator(A):
   ...

class MyClass:
   ...

MyClass = my_decorator(MyClass())

obj = MyClass()

#Like function decorators, the new (decorated) class is available under the name 'MyClass' and is used to create an instance. The original class named 'MyClass' is no longer available in your name space. 
#The callable object returned by the class decorator creates and returns a new instance of the original class, extended in some way.


#1.11
#a class decorated with a function that allows us to monitor the fact that some code gets access to the class object attributes.
class Car:
    def __init__(self, VIN):
        self.mileage = 0
        self.VIN = VIN

car = Car('ABC123')
print('The mileage is', car.mileage)
print('The VIN is', car.VIN)
>>
The mileage is 0
The VIN is ABC123

