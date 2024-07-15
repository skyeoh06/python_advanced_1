#1.3
#Encapsulation
#Python allows you to control access to attributes with the built-in property() function and corresponding decorator @property.
#This decorator plays a very important role:

#it designates a method which will be called automatically when another object wants to read the encapsulated attribute value;
#the name of the designated method will be used as the name of the instance attribute corresponding to the encapsulated attribute;
#it should be defined before the method responsible for setting the value of the encapsulated attribute, and before the method responsible for deleting the encapsulated attribute.
class TankError(Exception):
    pass


class Tank:
    def __init__(self, capacity):
        self.capacity = capacity
        self.__level = 0

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, amount):
        if amount > 0:
            # fueling
            if amount <= self.capacity:
                self.__level = amount
            else:
                raise TankError('Too much liquid in the tank')
        elif amount < 0:
            raise TankError('Not possible to set negative liquid level')

    @level.deleter
    def level(self):
        if self.__level > 0:
            print('It is good to remember to sanitize the remains from the tank!')
        self.__level = None


#that every Tank class object has a __level attribute, and the class delivers the methods responsible for handling access to that attribute.
#The @property decorated method is a method to be called when some other code wants to read the level of liquid in our tank. We call such a read method getter.
#Pay attention to the fact that the method following the decorator gives the name (tank) to the attribute visible outside of the class.
#@tank.setter() – designates the method called for setting the encapsulated attribute value;
#@tank.deleter() – designates the method called when other code wants to delete the encapsulated attribute.
#As those attribute name repetitions could be misleading, let's explain the naming convention:

#the getter method is decorated with '@property'. It designates the name of the attribute to be used by the external code;
#the setter method is decorated with '@name.setter'. The method name should be the attribute name;
#the deleter method is decorated with '@name.deleter'. The method name should should be the attribute name.
class TankError(Exception):
    pass


class Tank:
    def __init__(self, capacity):
        self.capacity = capacity
        self.__level = 0

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, amount):
        if amount > 0:
            # fueling
            if amount <= self.capacity:
                self.__level = amount
            else:
                raise TankError('Too much liquid in the tank')
        elif amount < 0:
            raise TankError('Not possible to set negative liquid level')

    @level.deleter
    def level(self):
        if self.__level > 0:
            print('It is good to remember to sanitize the remains from the tank!')
        self.__level = None

# our_tank object has a capacity of 20 units
our_tank = Tank(20)

# our_tank's current liquid level is set to 10 units
our_tank.level = 10
print('Current liquid level:', our_tank.level)

# adding additional 3 units (setting liquid level to 13)
our_tank.level += 3
print('Current liquid level:', our_tank.level)

# let's try to set the current level to 21 units
# this should be rejected as the tank's capacity is 20 units
try:
    our_tank.level = 21
except TankError as e:
    print('Trying to set liquid level to 21 units, result:', e)

# similar example - let's try to add an additional 15 units
# this should be rejected as the total capacity is 20 units
try:
    our_tank.level += 15
except TankError as e:
    print('Trying to add an additional 15 units, result:', e)

# let's try to set the liquid level to a negative amount
# this should be rejected as it is senseless
try:
    our_tank.level = -3
except TankError as e:
    print('Trying to set liquid level to -3 units, result:', e)

print('Current liquid level:', our_tank.level)

del our_tank.level
>>
Current liquid level: 10
Current liquid level: 13
Trying to set liquid level to 21 units, result: Too much liquid in the tank
Trying to add an additional 15 units, result: Too much liquid in the tank
Trying to set liquid level to -3 units, result: Not possible to set negative liquid level
Current liquid level: 13
It is good to remember to sanitize the remains from the tank!

#access to the __level attribute is handled by the designated methods by allowing the other code accessing the 'level' attribute. 
#The other code can make use of the 'level' attribute in a convenient way, without even knowing about the logic hidden behind it. So, whenever you'd like to control access to an attribute, you should prepare dedicated properties, 
#because properties control only designated attributes.
#properties are inherited, so you can call setters as if they were attributes.

