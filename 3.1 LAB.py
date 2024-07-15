#1.4
#Advanced exceptions - named attributes
#let's look at a typical try ... except statement.
try:
    print(int('a'))
except ValueError as e_variable:
    print(e_variable.args)

>> ("invalid literal for int() with base 10: 'a'",)

#The except clause may specify a variable after the exception name. In this example it’s an e_variable. This variable is bound to an exception instance with the arguments stored in the args attribute of the e_variable object.
try:
    import abcdefghijk

except ImportError as e:
    print(e.args)
    print(e.name)
    print(e.path)

>>
("No module named 'abcdefghijk'",)
abcdefghijk
None

#The ImportError exception – raised when the import statement has trouble trying to load a module. The attributes are:

#name – represents the name of the module that was attempted to be imported;
#path – represents the path to any file which triggered the exception, respectively. Could be None.

#1.5
#The UnicodeError exception – raised when a Unicode-related encoding or decoding error occurs. It is a subclass of ValueError.
#The UnicodeError has attributes that describe an encoding or decoding error.

#encoding – the name of the encoding that raised the error.
#reason – a string describing the specific codec error.
#object – the object the codec was attempting to encode or decode.
#start – the first index of invalid data in the object.
#end – the index after the last invalid data in the object.
try:
    b'\x80'.decode("utf-8")
except UnicodeError as e:
    print(e)
    print(e.encoding)
    print(e.reason)
    print(e.object)
    print(e.start)
    print(e.end)
>>
'utf-8' codec can't decode byte 0x80 in position 0: invalid start byte
utf-8
invalid start byte
b'\x80'
0
1

#1.7
a_list = ['First error', 'Second error']

try:
    print(a_list[3])
except Exception as e:
    print(0 / 0)

>> 
print(a_list[3])
IndexError: list index out of range

During handling of the above exception, another exception occurred:

print(0 / 0)
ZeroDivisionError: division by zero
#The result of the code execution contains a message that joins the subsequent tracebacks:
#During handling of the above exception, another exception occurred:
#It contains an interesting piece of information indicating that we’ve just witnessed a chain of exceptions.

#1.8
#The original exception object e is now being referenced by the __context__ attribute of the following exception f.
#The except Exception clause is a wide one and normally should be used as a last resort to catch all unhandled exceptions. It’s so wide because we don’t know what kind of exception might occur.
a_list = ['First error', 'Second error']

try:
    print(a_list[3])
except Exception as e:
    try:
        # the following line is a developer mistake - they wanted to print progress as 1/10	but wrote 1/0
        print(1 / 0)
    except ZeroDivisionError as f:
        print('Inner exception (f):', f)
        print('Outer exception (e):', e)
        print('Outer exception referenced:', f.__context__)
        print('Is it the same object:', f.__context__ is e)
>>
Inner exception (f): division by zero
Outer exception (e): list index out of range
Outer exception referenced: list index out of range
Is it the same object: True

#1.9
#Advanced exceptions - explicitly chained exceptions
#This time we'd like to convert an explicit type of exception object to another type of exception object at the moment when the second exception is occurring.
#Imagine that your code is responsible for the final checking process before the rocket is launched. The list of checks is a long one, and different checks could result in different exceptions.
#But as it is a very serious process, you should be sure that all checks are passed. If any fails, it should be marked in the log book and re-checked next time.
#Now you see that it would be convenient to convert each type of exception into its own exception (like RocketNotReadyError) and to log the origin of the exception.
class RocketNotReadyError(Exception):
    pass


def personnel_check():
    try:
        print("\tThe captain's name is", crew[0])
        print("\tThe pilot's name is", crew[1])
        print("\tThe mechanic's name is", crew[2])
        print("\tThe navigator's name is", crew[3])
    except IndexError as e:
        raise RocketNotReadyError('Crew is incomplete') from e

crew = ['John', 'Mary', 'Mike']
print('Final check procedure')

personnel_check()
>>
Final check procedure
	The captain's name is John
	The pilot's name is Mary
	The mechanic's name is Mike
print("\tThe navigator's name is", crew[3])
IndexError: list index out of range
The above exception was the direct cause of the following exception:
    personnel_check()
    raise RocketNotReadyError('Crew is incomplete') from e
__main__.RocketNotReadyError: Crew is incomplete

#1.10
#To catch the cause of the RocketNotReadyError exception, you should access the __cause__ attribute of the RocketNotReadyError object.
class RocketNotReadyError(Exception):
    pass


def personnel_check():
    try:
        print("\tThe captain's name is", crew[0])
        print("\tThe pilot's name is", crew[1])
        print("\tThe mechanic's name is", crew[2])
        print("\tThe navigator's name is", crew[3])
    except IndexError as e:
        raise RocketNotReadyError('Crew is incomplete') from e

crew = ['John', 'Mary', 'Mike']
print('Final check procedure')

try:
    personnel_check()
except RocketNotReadyError as f:
    print('General exception: "{}", caused by "{}"'.format(f, f.__cause__))
>>
Final check procedure
	The captain's name is John
	The pilot's name is Mary
	The mechanic's name is Mike
General exception: "Crew is incomplete", caused by "list index out of range"

#1.11
#Have a look at an extended checklist script.
#Pay attention to the fact that thanks to polymorphism and explicit chaining, our approach has become more generic: we are able to run two different checks, each returning a different exception type.
#And we’re still able to handle them correctly, as we’re hiding some details behind the RocketNotReadyError exception object.
class RocketNotReadyError(Exception):
    pass


def personnel_check():
    try:
        print("\tThe captain's name is", crew[0])
        print("\tThe pilot's name is", crew[1])
        print("\tThe mechanic's name is", crew[2])
        print("\tThe navigator's name is", crew[3])
    except IndexError as e:
        raise RocketNotReadyError('Crew is incomplete') from e


def fuel_check():
    try:
        print('Fuel tank is full in {}%'.format(100 / 0))
    except ZeroDivisionError as e:
        raise RocketNotReadyError('Problem with fuel gauge') from e


crew = ['John', 'Mary', 'Mike']
fuel = 100
check_list = [personnel_check, fuel_check]

print('Final check procedure')

for check in check_list:
    try:
        check()
    except RocketNotReadyError as f:
        print('RocketNotReady exception: "{}", caused by "{}"'.format(f, f.__cause__))

>>

 
 Sandbox
Code
class RocketNotReadyError(Exception):
pass


def personnel_check():
try:
print("\tThe captain's name is", crew[0])
print("\tThe pilot's name is", crew[1])
print("\tThe mechanic's name is", crew[2])
print("\tThe navigator's name is", crew[3])
except IndexError as e:
raise RocketNotReadyError('Crew is incomplete') from e


def fuel_check():
try:
print('Fuel tank is full in {}%'.format(100 / 0))
except ZeroDivisionError as e:
raise RocketNotReadyError('Problem with fuel gauge') from e


crew = ['John', 'Mary', 'Mike']
fuel = 100
check_list = [personnel_check, fuel_check]

print('Final check procedure')

for check in check_list:
try:
check()
except RocketNotReadyError as f:
print('RocketNotReady exception: "{}", caused by "{}"'.format(f, f.__cause__))
class RocketNotReadyError(Exception):
    pass


Console 
Final check procedure
	The captain's name is John
	The pilot's name is Mary
	The mechanic's name is Mike
RocketNotReady exception: "Crew is incomplete", caused by "list index out of range"
RocketNotReady exception: "Problem with fuel gauge", caused by "division by zero"

#1.12
#Scenario
#Try to extend the check list script to handle more different checks, all reported as RocketNotReady exceptions.
#Add your own checks for: batteries and circuits.
class RocketNotReadyError(Exception):
    pass


def personnel_check():
    try:
        print("\tThe captain's name is", crew[0])
        print("\tThe pilot's name is", crew[1])
        print("\tThe mechanic's name is", crew[2])
        print("\tThe navigator's name is", crew[3])
    except IndexError as e:
        raise RocketNotReadyError('Crew is incomplete') from e


def fuel_check():
    try:
        print('Fuel tank is full in {}%'.format(100/0))
    except ZeroDivisionError as e:
        raise RocketNotReadyError('Problem with fuel gauge') from e

def batteries_check():
    # add your own implementation
    try:
        print('Batteries is full in {}%'.format(100/0))
    except ZeroDivisionError as e:
        raise RocketNotReadyError('Problem with batteries gauge') from e

def circuits_check():
    # add your own implementation
    try:
        print('Circuits is full in {}%'.format(100/0))
    except ZeroDivisionError as e:
        raise RocketNotReadyError('Problem with circuits gauge') from e

crew = ['John', 'Mary', 'Mike']
fuel = 100
check_list = [personnel_check, fuel_check, batteries_check, circuits_check]

print('Final check procedure')

for check in check_list:
    try:
        check()
    except RocketNotReadyError as f:
        print('RocketNotReady exception: "{}", caused by "{}"'.format(f, f.__cause__))

>>
Final check procedure
	The captain's name is John
	The pilot's name is Mary
	The mechanic's name is Mike
RocketNotReady exception: "Crew is incomplete", caused by "list index out of range"
RocketNotReady exception: "Problem with fuel gauge", caused by "division by zero"
RocketNotReady exception: "Problem with batteries gauge", caused by "division by zero"
RocketNotReady exception: "Problem with circuits gauge", caused by "division by zero"

#1.13
#Advanced exceptions - the traceback attribute
#Each exception object owns a __traceback__ attribute.
#Python allows us to operate on the traceback details because each exception object (not only chained ones) owns a __traceback__ attribute.
class RocketNotReadyError(Exception):
    pass


def personnel_check():
    try:
        print("\tThe captain's name is", crew[0])
        print("\tThe pilot's name is", crew[1])
        print("\tThe mechanic's name is", crew[2])
        print("\tThe navigator's name is", crew[3])
    except IndexError as e:
        raise RocketNotReadyError('Crew is incomplete') from e


crew = ['John', 'Mary', 'Mike']

print('Final check procedure')

try:
    personnel_check()
except RocketNotReadyError as f:
    print(f.__traceback__)
    print(type(f.__traceback__))
>>
Final check procedure
	The captain's name is John
	The pilot's name is Mary
	The mechanic's name is Mike
<traceback object at 0x7f2b0038eb90>
<class 'traceback'>

#1.14
#To achieve this, we could use the format_tb() method delivered by the built-in traceback module to get a list of strings describing the traceback.
#We could use the print_tb() method, also delivered by the traceback module, to print strings directly to the standard output.
#The corresponding output reveals the sequence of exceptions and proves that the execution was not interrupted by the exceptions because we see the final wording.
    import traceback

class RocketNotReadyError(Exception):
    pass


def personnel_check():
    try:
        print("\tThe captain's name is", crew[0])
        print("\tThe pilot's name is", crew[1])
        print("\tThe mechanic's name is", crew[2])
        print("\tThe navigator's name is", crew[3])
    except IndexError as e:
        raise RocketNotReadyError('Crew is incomplete') from e


crew = ['John', 'Mary', 'Mike']

print('Final check procedure')

try:
    personnel_check()
except RocketNotReadyError as f:
    print(f.__traceback__)
    print(type(f.__traceback__))
    print('\nTraceback details')
    details = traceback.format_tb(f.__traceback__)
    print("\n".join(details))

print('Final check is over')
>>
Final check procedure
	The captain's name is John
	The pilot's name is Mary
	The mechanic's name is Mike
<traceback object at 0x7f47c252b500>
<class 'traceback'>

Traceback details
  File "main.py", line 22, in <module>
    personnel_check()

  File "main.py", line 14, in personnel_check
    raise RocketNotReadyError('Crew is incomplete') from e

Final check is over

#In real life development projects, you may make use of logged tracebacks after comprehensive test sessions to gather statistics or even automate bug reporting processes.
