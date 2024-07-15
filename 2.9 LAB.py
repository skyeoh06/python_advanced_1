#1.2
#Something that’s worth commenting on is that we have delivered:

#a static, dedicated method for checking argument types. As we have delegated this responsibility to only one method, the code will be shorter, cleaner and easier to maintain. We'll make use of this method a few times. In case the argument's type is not an integer, a ValueError exception is raised;
#an overridden method __setitem__, which is a magic method (mind the underscores) responsible for inserting (overwriting) an element at a given position. This method calls the check_value_type() method and later calls the genuine method __setitem__ which comes from the parent class, which does the rest of the job (sets the validated value at a given position). Now you can sigh – “oh, what a great ability!”
#an overridden method, append(), which is responsible for appending an element to the end of the list. This method follows the previous way of dealing with a new element;
#an overridden method, extend(), to verify and add a collection of elements to the object.
#What have we not delivered?

#All the remaining methods have remained unchanged, so our new list-like class will still behave like its parent in those places.
class IntegerList(list):

    @staticmethod
    def check_value_type(value):
        if type(value) is not int:
            raise ValueError('Not an integer type')

    def __setitem__(self, index, value):
        IntegerList.check_value_type(value)
        list.__setitem__(self, index, value)

    def append(self, value):
        IntegerList.check_value_type(value)
        list.append(self, value)

    def extend(self, iterable):
        for element in iterable:
            IntegerList.check_value_type(element)

        list.extend(self, iterable)


int_list = IntegerList()

int_list.append(66)
int_list.append(22)
print('Appending int elements succeed:', int_list)

int_list[0] = 31
print('Inserting int element succeed:', int_list)

int_list.extend([2, 3])
print('Extending with int elements succeed:', int_list)

try:
    int_list.append('8-10')
except ValueError:
    print('Appending string failed')

try:
    int_list[0] = '10/11'
except ValueError:
    print('Inserting string failed')

try:
    int_list.extend([997, '10/11'])
except ValueError:
    print('Extending with ineligible element failed')

print('Final result:', int_list)
>>
Appending int elements succeed: [66, 22]
Inserting int element succeed: [31, 22]
Extending with int elements succeed: [31, 22, 2, 3]
Appending string failed
Inserting string failed
Extending with ineligible element failed
Final result: [31, 22, 2, 3]

#To make our newly-created class fully functional, it’s necessary to deliver implementations for the methods:

insert(index, object)
__add__()
#These implementations should be fairly similar to the implementations delivered above (validate the type and then call the corresponding superclass method).

#1.3
#we’ll create a class based on Python’s built-in dictionary, which will be equipped with logging mechanisms for details of writing and reading operations performed on the elements of our dictionary.
#In other words, we are arming a Python dictionary with the ability to log details (time and operation type) of:

class instantiation;
read access;
new element creation or update.
#A few notes for the code implementing the MonitoredDict class:

#we have subclassed a dict class with a new __init__() method that calls the __init__() method from its super class. Additionally, it creates a list (self.log) that plays the role of a log book. Finally, the log book is populated with a message noting that the object has been created;
#we have created the log_timestamp() method that appends crucial information to the self.log attribute;
#we have overridden two methods inherent for the dictionary class (__getitem__() and __setitem__()) to deliver a richer implementation that logs activities. But don’t worry, we’re not losing anything from the parent dictionary class, because we’re still calling the corresponding methods.
from datetime import datetime


class MonitoredDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.log = list()
        self.log_timestamp('MonitoredDict created')

    def __getitem__(self, key):
        val = super().__getitem__(key)
        self.log_timestamp('value for key [{}] retrieved'.format(key))
        return val

    def __setitem__(self, key, val):
        super().__setitem__(key, val)
        self.log_timestamp('value for key [{}] set'.format(key))

    def log_timestamp(self, message):
        timestampStr = datetime.now().strftime("%Y-%m-%d (%H:%M:%S.%f)")
        self.log.append('{} {}'.format(timestampStr, message))


kk = MonitoredDict()
kk[10] = 15
kk[20] = 5

print('Element kk[10]:', kk[10])
print('Whole dictionary:', kk)
print('Our log book:\n')
print('\n'.join(kk.log))
>>
Element kk[10]: 15
Whole dictionary: {10: 15, 20: 5}
Our log book:

2024-07-15 (06:50:03.945351) MonitoredDict created
2024-07-15 (06:50:03.945408) value for key [10] set
2024-07-15 (06:50:03.945426) value for key [20] set
2024-07-15 (06:50:03.945440) value for key [10] retrieved

#1.4
#The IBAN Only Dictionary
#The “Integer only list” is an example of the employment of a subclassed built-in list to check the types of elements being added to the list. How about checking the values of the keys being used when new elements are added to the dictionary?
#IBAN is an algorithm used by European banks to specify account numbers. The standard name IBAN (International Bank Account Number) provides a simple and fairly reliable method of validating the account numbers against simple typos that can occur during rewriting of the number, 
#e.g., from paper documents, like invoices or bills, into computers.
#n IBAN-compliant account number consists of:

#a two-letter country code taken from the ISO 3166-1 standard (e.g., FR for France, GB for the United Kingdom, DE for Germany, and so on)
#two check digits used to perform the validity checks – fast and simple, but not fully reliable, tests, showing whether a number is invalid (distorted by a typo) or seems to be good;
#the actual account number (up to 30 alphanumeric characters – the length of that part depends on the country)
# IBAN Validator

iban = input("Enter IBAN, please: ")
iban = iban.replace(' ','')
if not iban.isalnum():
    print("You have entered invalid characters.")
elif len(iban) < 15:
    print("IBAN entered is too short.")
elif len(iban) > 31:
    print("IBAN entered is too long.")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ''
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A'))
    ibann = int(iban2)
    if ibann % 97 == 1:
        print("IBAN entered is valid.")
    else:
        print("IBAN entered is invalid.")
>>
Enter IBAN, please: GB72 HBZU 7006 7212 1253 00
IBAN entered is valid.
Enter IBAN, please: DE02100100100152517108
IBAN entered is valid.

#1.5
#To sum up, our validateIBAN(iban) function:

#requires a parameter; it is a string to check whether it contains an IBAN-compliant account number;
#raises an IBANValidationError exception when the supplied string carries an incorrectly formulated account number;
#returns a True value when the account number conforms to all IBAN requirements.
class IBANValidationError(Exception):
    pass


def validateIBAN(iban):
    iban = iban.replace(' ', '')

    if not iban.isalnum():
        raise IBANValidationError("You have entered invalid characters.")

    elif len(iban) < 15:
        raise IBANValidationError("IBAN entered is too short.")

    elif len(iban) > 31:
        raise IBANValidationError("IBAN entered is too long.")

    else:
        iban = (iban[4:] + iban[0:4]).upper()
        iban2 = ''
        for ch in iban:
            if ch.isdigit():
                iban2 += ch
            else:
                iban2 += str(10 + ord(ch) - ord('A'))
        ibann = int(iban2)

        if ibann % 97 != 1:
            raise IBANValidationError("IBAN entered is invalid.")

        return True


test_keys = ['GB72 HBZU 7006 7212 1253 01', 'FR76 30003 03620 00020216907 50', 'DE02100100100152517108' ]

for key in test_keys:
    try:
        print('Status of "{}" validation: '.format(key))
        validateIBAN(key)
    except IBANValidationError as e:
        print("\t{}".format(e))
    else:
        print("correct")
>>
Status of "GB72 HBZU 7006 7212 1253 01" validation: 
	IBAN entered is invalid.
Status of "FR76 30003 03620 00020216907 50" validation: 
correct
Status of "DE02100100100152517108" validation: 
correct

#1.6
#Having a validateIBAN() function in place, we can write our own class that inherits after a built-in dict class.
#In this implementation, we have delivered the method __setitem__() which calls validateIBAN() and on success calls the genuine __setitem__() method. This piece of code is responsible for statements like:

my_dict[key] = value

#We have also delivered the method update() which iterates the parameters passed, and for each correct pair calls the __setitem__() method
import random


class IBANValidationError(Exception):
    pass


class IBANDict(dict):
    def __setitem__(self, _key, _val):
        if validateIBAN(_key):
            super().__setitem__(_key, _val)

    def update(self, *args, **kwargs):
        for _key, _val in dict(*args, **kwargs).items():
            self.__setitem__(_key, _val)


def validateIBAN(iban):
    iban = iban.replace(' ', '')

    if not iban.isalnum():
        raise IBANValidationError("You have entered invalid characters.")

    elif len(iban) < 15:
        raise IBANValidationError("IBAN entered is too short.")

    elif len(iban) > 31:
        raise IBANValidationError("IBAN entered is too long.")

    else:
        iban = (iban[4:] + iban[0:4]).upper()
        iban2 = ''
        for ch in iban:
            if ch.isdigit():
                iban2 += ch
            else:
                iban2 += str(10 + ord(ch) - ord('A'))
        ibann = int(iban2)

        if ibann % 97 != 1:
            raise IBANValidationError("IBAN entered is invalid.")

        return True


my_dict = IBANDict()
keys = ['GB72 HBZU 7006 7212 1253 00', 'FR76 30003 03620 00020216907 50', 'DE02100100100152517108']

for key in keys:
    my_dict[key] = random.randint(0, 1000)

print('The my_dict dictionary contains:')
for key, value in my_dict.items():
    print("\t{} -> {}".format(key, value))

try:
    my_dict.update({'dummy_account': 100})
except IBANValidationError:
    print('IBANDict has protected your dictionary against incorrect data insertion')




>>
The my_dict dictionary contains:
	GB72 HBZU 7006 7212 1253 00 -> 693
	FR76 30003 03620 00020216907 50 -> 674
	DE02100100100152517108 -> 727
IBANDict has protected your dictionary against incorrect data insertion
