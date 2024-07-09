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
