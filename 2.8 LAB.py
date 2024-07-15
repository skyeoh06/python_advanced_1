#1.2
#Composition vs Inheritance
#Inheritance is not the only way of constructing adaptable objects. You can achieve similar goals by using a concept named composition.
#This concept models another kind of relation between objects; it models what is called a has a relation.

#Examples:

#a Laptop has a network card;
#a Hovercraft has a specific engine.
#Composition is the process of composing an object using other different objects. The objects used in the composition deliver a set of desired traits (properties and/or methods) so we can say that they act like blocks used to build a more complicated structure.

#It can be said that:

#inheritance extends a class's capabilities by adding new components and modifying existing ones; in other words, the complete recipe is contained inside the class itself and all its ancestors; the object takes all the class's belongings and makes use of them;
#composition projects a class as a container (called a composite) able to store and use other objects (derived from other classes) where each of the objects implements a part of a desired class's behavior. It’s worth mentioning that blocks are loosely coupled with the composite, and those blocks could be exchanged any time, even during program runtime.

#1.3
#The “Car” class is loosely coupled with the “engine” component. It’s a composite object.
#The main advantages are:

#whenever a change is applied to the engine object, it does not influence the “Car” class object structure;
#you can decide what your car should be equipped with.
class Car:
    def __init__(self, engine):
        self.engine = engine


class GasEngine:
    def __init__(self, horse_power):
        self.hp = horse_power

    def start(self):
        print('Starting {}hp gas engine'.format(self.hp))


class DieselEngine:
    def __init__(self, horse_power):
        self.hp = horse_power

    def start(self):
        print('Starting {}hp diesel engine'.format(self.hp))


my_car = Car(GasEngine(300))
my_car.engine.start()
my_car.engine = DieselEngine(221)
my_car.engine.start()
>>
Starting 300hp gas engine
Starting 221hp diesel engine

#1.5
#Which way should you choose?
#Before we answer the question, let's mention a few more things:

#inheritance and composition are not mutually exclusive. Real-life problems are hardly every pure “is a” or “has a” cases;
#treat both inheritance and composition as supplementary means for solving problems;
#there is nothing wrong with composing objects of ... classes that were built using inheritance. The next example code should shed some light on this case.
#If the problem can be modeled using an “is a” relation, then the inheritance approach should be implemented.
#Otherwise, if the problem can be modeled using a “has a” relation, then the choice is clear – composition is the solution.
class Base_Computer:
    def __init__(self, serial_number):
        self.serial_number = serial_number


class Personal_Computer(Base_Computer):
    def __init__(self, sn, connection):
        super().__init__(sn)
        self.connection = connection
        print('The computer costs $1000')


class Connection:
    def __init__(self, speed):
        self.speed = speed

    def download(self):
        print('Downloading at {}'.format(self.speed))


class DialUp(Connection):
    def __init__(self):
        super().__init__('9600bit/s')

    def download(self):
        print('Dialling the access number ... '.ljust(40), end='')
        super().download()


class ADSL(Connection):
    def __init__(self):
        super().__init__('2Mbit/s')

    def download(self):
        print('Waking up modem  ... '.ljust(40), end='')
        super().download()


class Ethernet(Connection):
    def __init__(self):
        super().__init__('10Mbit/s')

    def download(self):
        print('Constantly connected... '.ljust(40), end='')
        super().download()

# I started my IT adventure with an old-school dial up connection
my_computer = Personal_Computer('1995', DialUp())
my_computer.connection.download()

# then in the year 1999 I got ADSL
my_computer.connection = ADSL()
my_computer.connection.download()

# finally I upgraded to Ethernet
my_computer.connection = Ethernet()
my_computer.connection.download()


my_computer = Personal_Computer('2022', Ethernet())
my_computer.connection.download()
>>
The computer costs $1000
Dialling the access number ...          Downloading at 9600bit/s
Waking up modem  ...                    Downloading at 2Mbit/s
Constantly connected...                 Downloading at 10Mbit/s
The computer costs $1000
Constantly connected...                 Downloading at 10Mbit/s

#There is a “Base_Computer” class that represents a generic computer. A generic computer has only a serial number;
#there is a “Personal_Computer” class that is built upon the “Base_Computer” class and represents a computer that is able to connect to the internet;
#there is a generic “Connection” class that holds information about the connection speed and handles the download() method. This class is independent of any computer class;
#there are the “Connection” subclasses, more specialized than the “Connection” class:
“Dialup”
“ADSL”
“Ethernet”
#* When we start with our personal computer, we set the serial number to 1995 and equip it with a dialup connection. This an example of composition.

#It is possible to download some data using a slow dialup connection;
#later, we equip our personal computer with a more advanced connection device. There is no need to recreate the computer object – we just arm it with a new component;
#the last steps are about arming our old computer with a fast connection and downloading some data.
