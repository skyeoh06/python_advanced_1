#1.3
#Abstract classes
class BluePrint:
    def hello(self):
        print('Nothing is blue unless you need it')


bp = BluePrint()
bp.hello()
>> Nothing is blue unless you need it

#1.4
#Python has come up with a module which provides the helper class for defining Abstract Base Classes (ABC) and that module name is abc.
#The ABC allows you to mark classes as abstract ones and distinguish which methods of the base abstract class are abstract. A method becomes abstract by being decorated with an @abstractmethod decorator.
#To start with ABC you should:

import the abc module;
#make your base class inherit the helper class ABC, which is delivered by the abc module;
#decorate abstract methods with @abstractmethod, which is delivered by the abc module.
import abc

class BluePrint(abc.ABC):
    @abc.abstractmethod
    def hello(self):
        pass

class GreenField(BluePrint):
    def hello(self):
        print('Welcome to Green Field!')


gf = GreenField()
gf.hello()

>> Welcome to Green Field!

#1.5
#to instantiate the BluePrint class:
bp = BluePrint()
>>
bp = BluePrint()
TypeError: Can't instantiate abstract class BluePrint with abstract methods hello

#indicates that:

#it’s possible to instantiate the GreenField class and call the hello method, because the Python developer has provided a concrete definition of the hello method.
#In other words, the Python developer has overridden the abstract method hello with their own implementation. When the base class provides more abstract methods, 
#all of them must be overridden in a subclass before the subclass can be instantiated.
#Python raises a TypeError exception when we try to instantiate the base BluePrint class, because it contains an abstract method.

#1.6
#inherit the abstract class and forget about overriding the abstract method by creating a RedField class that does not override the hello method.
import abc


class BluePrint(abc.ABC):
    @abc.abstractmethod
    def hello(self):
        pass


class GreenField(BluePrint):
    def hello(self):
        print('Welcome to Green Field!')


class RedField(BluePrint):
    def yellow(self):
        pass


gf = GreenField()
gf.hello()

rf = RedField()
>>
rf = RedField()
TypeError: Can't instantiate abstract class RedField with abstract methods hello

#ndicates that:

#it’s possible to instantiate the GreenField class and call the hello method;
#the RedField class is still recognized as an abstract one, because it inherits all elements of its super class, which is abstract, and the RedField class does not override the abstract hello method.

#1.7
#Multiple inheritance
#When you plan to implement a multiple inheritance from abstract classes, remember that an effective subclass should override all abstract methods inherited from its super classes.
#Summary:
#Abstract Base Class (ABC) is a class that cannot be instantiated. Such a class is a base class for concrete classes;
#ABC can only be inherited from;
#we are forced to override all abstract methods by delivering concrete method implementations.
#A note:

#It’s tempting to call a module “abc” and then try to import it, but by doing so Python imports the module containing the ABC class instead of your local file. 
#This could cause some confusion – why does such a common name as “abc” conflict with my simple module “abc”?

