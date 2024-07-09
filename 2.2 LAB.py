#1.3
#Inheritance and polymorphism — Single inheritance vs. multiple inheritance
#The ambiguity that arises here is caused by the fact that class B and class C are inherited from superclass A, and class D is inherited from both classes B and C. If you want to call the method info(), which part of the code would be executed then?
class A:
    def info(self):
        print('Class A')

class B(A):
    def info(self):
        print('Class B')

class C(A):
    def info(self):
        print('Class C')

class D(B, C):
    pass

D().info()

>> Class B

#In the multiple inheritance scenario, any specified attribute is searched for first in the current class. If it is not found, the search continues into the direct parent classes in depth-first level (the first level above), from the left to the right, according to the class definition. 
#This is the result of the MRO algorithm.
#class D does not define the method info(), so Python has to look for it in the class hierarchy;
#class D is constructed in this order:
#the definition of class B is fetched;
#the definition of class C is fetched;
#Python finds the requested method in the class B definition and stops searching;
#Python executes the method.

#1.4
#Possible pitfalls — MRO inconsistency
#MRO can report definition inconsistencies when a subtle change in the class D definition is introduced, which is possible when you work with complex class hierarchies.
#change B to A
class A:
    def info(self):
        print('Class A')

class B(A):
    def info(self):
        print('Class B')

class C(A):
    def info(self):
        print('Class C')

class D(A, C):
    pass

D().info()
>> class D(A, C):
TypeError: Cannot create a consistent method resolution
order (MRO) for bases A, C

#This message informs us that the MRO algorithm had problems determining which method (originating from the A or C classes) should be called.


#1.5
#Due to MRO, you should knowingly list the superclasses in the subclass definition. In the following example, class D is based on classes B and C, whereas class E is based on classes C and B (the order matters!).
class A:
    def info(self):
        print('Class A')

class B(A):
    def info(self):
        print('Class B')

class C(A):
    def info(self):
        print('Class C')

class D(B, C):
    pass

class E(C, B):
    pass

D().info()
>> Class B
E().info()
>> Class C

#As a result, those classes can behave totally differently, because the order of the superclasses is different.

#1.7
#polymorphism on integers and strings
a = 10
print(a.__add__(20))
>> 30
b = 'abc'
print(b.__add__('def'))
>> abcdef

#1.8
#two pillars of OOP combined
#One way to carry out polymorphism is inheritance, when subclasses make use of base class methods, or override them. By combining both approaches, the programmer is given a very convenient way of creating applications, as:
#most of the code could be reused and only specific methods are implemented, which saves a lot of development time and improves code quality;
#the code is clearly structured;
#there is a uniform way of calling methods responsible for the same operations, implemented accordingly for the types.
#Remember: You can use inheritance to create polymorphic behavior, and usually that's what you do, but that's not what polymorphism is about.

class Device:
    def turn_on(self):
        print('The device was turned on')

class Radio(Device):
    pass

class PortableRadio(Device):
    def turn_on(self):
        print('PortableRadio type object was turned on')

class TvSet(Device):
    def turn_on(self):
        print('TvSet type object was turned on')

device = Device()
radio = Radio()
portableRadio = PortableRadio()
tvset = TvSet()

for element in (device, radio, portableRadio, tvset):
    element.turn_on()

>>
The device was turned on
The device was turned on
PortableRadio type object was turned on
TvSet type object was turned on

#inheritance: class Radio inherits the turn_on() method from its superclass — that is why we see The device was turned on string twice. Other subclasses override that method and as a result we see different lines being printed;
#polymorphism: all class instances allow the calling of the turn_on() method, even when you refer to the objects using the arbitrary variable element.

#1.9
#duck typing
#Duck typing is a fancy name for the term describing an application of the duck test: "If it walks like a duck and it quacks like a duck, then it must be a duck", which determines whether an object can be used for a particular purpose. 
#An object's suitability is determined by the presence of certain attributes, rather than by the type of the object itself.
#In duck typing, we believe that objects own the methods that are called. If they do not own them, then we should be prepared to handle exceptions.
class Wax:
    def melt(self):
        print("Wax can be used to form a tool")

class Cheese:
    def melt(self):
        print("Cheese can be eaten")

class Wood:
    def fire(self):
        print("A fire has been started!")

for element in Wax(), Cheese(), Wood():
    try:
        element.melt()
    except AttributeError:
        print('No melt() method')
>>
Wax can be used to form a tool
Cheese can be eaten
No melt() method

#Let's talk about two things that share conceptually similar methods, but represent totally different things, like cheese and wax. Both can melt, and we use the melted forms for different purposes.
#Both the Wax and Cheese classes own melt() methods, but there is no relation between the two. Thanks to duck typing, we can call the melt() method. Unfortunatelly, the Wood class is not equipped with this method, so an AttributeError exception occurs.

#Summary:

#polymorphism is used when different class objects share conceptually similar methods (but are not always inherited)
#polymorphism leverages clarity and expressiveness of the application design and development;
#when polymorphism is assumed, it is wise to handle exceptions that could pop up.
