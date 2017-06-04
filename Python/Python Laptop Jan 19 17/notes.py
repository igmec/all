import sys
sys.exit(0)
#==========================================================================
#============================ Part I: Basics ==============================
#==========================================================================

#----------------------Chapter 1: Python Basics----------------------#

# - 'Alice' + 'Bob' = 'AliceBob'
# - 'Alice' * 5(int) = 'AliceAliceAliceAliceAlice'

print("What is your name?")
name = input()
length = len(name)

int('29') = 29
str(29) = '29'
float(29) = 29.0

#----------------------Chapter 2: Flow Control-----------------------#

True
False
and or not #(&& || !)
# ==   !=   <=   >=   <   >

if cond1 == True and cond2 == True:
    executeIfCode()
elif cond1 == False or (not (cond2 == False)):
    executeElifCode()
else:
    executeElseCode()


while cond1 == True:
    executeCodeInLoop()


for i in range(0,5,1): #--->(start, stop, step), stop not included in range
    executeCode5Times(i)


break    # will break out of the loop
continue # will return to the start of the loop for its next iteration


import random, module2, etc
from fibo import fib1, fib2 # the functions of fibo become functions of current script
from fibo import *          # same as above but all functions get imported

random.randint(1,10) # to use above random module
                     # 1 to 10 inclusive at both ends

import sys
sys.exit() # will exit whatever scrip running




#-----------------------Chapter 3: Functions------------------------#

def newFunc():
    executeFunctionCode()

def funcWithParams(name, idNum):
    print(name + ': ' + idNum)
    #Returns None value of the NoneType data type

def funcThatReturns(name, idNum):
    return name + ': ' + idNum

spam = print('Hello')
None == spam # == True

print('Hello', end='--') #default: end='\n'
print('World')  #---->    Hello--World
print('cats', 'dogs', 'mice', sep=' and ') #--->   cats and dogs and mice


try:
    print(42/0)
except ZeroDivisionError:
    print("Cannot divide by zero!")


#=-=-=-=-=-=-=-=-SCOPES-=-=-=--=-=-=-=-=#

#-----Ex. Local-----#

def spam():
    eggs = 'spam local'
    print(eggs) # prints 'spam local'

def bacon():
    eggs = 'bacon local'
    print(eggs) # prints 'bacon local'
    spam()
    print(eggs) # prints 'bacon local'

eggs = 'global'
bacon()
print(eggs) # prints 'global'

#--Prints-->
#bacon local
#spam local
#bacon local
#global


#-----Ex. Global-----#

def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)

#--Prints-->
#spam



#-----Ex. Global & Local-----#

def spam():
    global eggs
    eggs = 'spam' # this is the global

def bacon():
    eggs = 'bacon' # this is a local

def ham():
    print(eggs) # this is the global

eggs = 42 # this is the global
spam()
print(eggs)

#--Prints-->
#spam

#=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=#


#-------------------------Chapter 4: Lists--------------------------#

list = [1,2,3]
list = ['cat', 'dog', 'bird']
list = ['hello', 3.1415, True, None, 42]
list[0]     #---> 'hello'
list[-1]    #---> 42
list[1:4]   #---> [3.1415, True, None]
            # includes from index 1 up to 4 NOT INCLUDING stop index
list[1:-1]  #--->[3.1415, True, None]
list[:2] = list[0:2]
list[1:] = list[1:end]
list[:] = list[0:end]

2dlist = [['cat', 'bat'],
          [10, 20, 30, 40, 50]]
2dlist[0]     #---> ['cat', 'bat']
2dlist[1][2]  #---> 30
2dlist[1][-2] #---> 40

len(list) #---> 5
for i in range(len(list)):

[1, 2, 3] + ['A', 'B', 'C'] = [1, 2, 3, 'A', 'B', 'C']
['X', 'Y', 'Z'] * 3 = ['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']

spam = ['cat', 'bat', 'rat', 'elephant']
'rat' in spam   #---> True
del spam[2]     #---> ['cat', 'bat', 'elephant']
'rat' in spam   #---> False
'rat' not in spam #-> True

#for loops will iterate through succesive values in a list
for i in range(4): #is the same as writing
for i in [0,1,2,3]:

cat = ['fat', 'black', 'loud']
size, colour, disposition = cat
#number of list elements must match number of variables

#  +=  -=  *=  /=  %=

list = ['abc']
list *= 3 #---> ['abc', 'abc', 'abc']

spam = ['hello', 'hi', 'howdy', 'hey', 'hi']
spam.index('hi')        #---> 1  #only index of first value is returned
spam.index('bye')       #---> ValueError (not in list)
spam.append('sup')      #---> ['hello', 'hi', 'howdy', 'hey', 'hi', 'sup']
spam.insert(2, 'heya')  #---> ['hello', 'hi', 'heya', 'howdy', 'hey', 'hi', 'sup']
spam.remove('heya')     #---> ['hello', 'hi', 'howdy', 'hey', 'hi', 'sup']
spam.remove('heya')     #---> ValueError (not in list)
spam.sort()             #---> ['hello', 'hey', 'hi', 'hi', 'howdy', 'sup']
spam.sort(reverse=True) #---> ['sup', 'howdy', 'hi', 'hi', 'hey', 'hello']

ham = [1, 3, 'cat', 'sun']
ham.sort()  #---> TypeError (can't sort ints and strings)
# sort() uses ASCIIbetical order, capital 'Z' comes before lower-case 'a'
ham = ['a', 'z', 'A', 'Z',]
ham.sort(key=str.lower) #---> ['a', 'A', 'z', 'Z']

print('Four score and seven ' + \
      'years ago...')

# mutable - you can change the sequence (list)
# immutable - you can't change the sequence (strings, tuples)

eggs = ('hello', 42, 0.5)   # Tuple can't have its values altered
eggs = ('hello',)   # Use comma for single value in tuple

tuple(['cat', 'dog', 5])    #---> ('cat', 'dog', 5)
list(('cat', 'dog', 5))     #---> ['cat', 'dog', 5]
list('hello')   #---> ['h', 'e', 'l', 'l', 'o']

spam = 42 
cheese = spam  # This copies value of spam into cheese variable

import copy
spam = [42, 13, 3]
cheese = spam   # This makes cheese point to same list as spam
                # Changing one will change the other
cheese = copy.copy(spam)      # This copies spam list into new cheese list
cheese = copy.deepcopy(spam)  # This copies 2D lists into cheese


#----------------------Chapter 5: Dictionaries----------------------#

#Dictionaries use key-value pairs
#Dictionaries are unordered
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
myCat['size']   #---> 'fat'
myCat['age']    #---> KeyError

spam = {'color': 'red', 'age': 42}
for v in spam.values()
for k in spam.keys()
for i in spam.items()       #---> Returns tuples, ('color', 'red'), ('age', 42)
for k, v in spam.items()    #---> returns the key into k and the value into v

list(spam.keys())   #---> ['color', 'age']
list(spam.values()) #---> ['red', 42]
list(spam.items())  #---> [('color', 'red'), ('age', 42)]

'size' in spam              #is the same as spam.keys()
'size' in spam.keys()       #---> False
'red' in spam.values()      #---> True
'blue' not in spam.values() #---> True
('age', 27) in spam.items() #---> False

spam.get('color', 'white')  #---> 'red'
# returns 'white' by default if 'color' key not found

spam.setdefault('mass', 'large') #---> 'large'
spam.setdefault('mass', 'small') #---> 'large'
#if the 'mass' key isn't used, set it to 'large'
#if the key is used, return its value

import pprint
pprint.pprint(spam) #Pretty Print will print dictionaries and lists neatly

#-------Nested Dictionaries Example------#

allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}

def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('Number of things being brought:')
print(' - Apples ' + str(totalBrought(allGuests, 'apples')))




#------------------Chapter 6: Manipulating Strings------------------#

# String literals can be in 'Single Quotes' or "Double Quotes"
# \'   \"  \t   \n   \\
print(r,'Raw String ignores all escape characters and \n prints all backslashes(\\)')
#Raw strings useful for REGEX

print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob''')

#---PRINTS AS:---
#Dear Alice,

#Eve's cat has been arrested for catnapping, cat burglary, and extortion.

#Sincerely,
#Bob
#----------------

#Single line comment

""" Multi-
    line
    comment """

spam = 'Hello World!'
spam[0] #---> 'H'
spam[4] #---> 'o'
spam[-1] #--> '!'
spam[0:5] #-> 'Hello'
spam[:5] #--> 'Hello'
spam[6:] #--> 'world!'


'Hello' in 'Hello world!'   #---> True
'HELLO' in 'Hello world!'   #---> False
'WORLD' not in 'Hello world!' #-> True

spam.upper()    #---> 'HELLO WORLD!'
spam.lower()    #---> 'hello world!'

spam = 'hello'
spam.islower()  #---> True  (must have min one letter, otherwise false)
spam = 'abc123'
spam.islower()  #---> True

spam = 'HELLO'
spam.isupper()  #---> True
spam = '12345'
spam.isupper()  #---> False


spam.isalpha()      #True if only letters, not blank
spam.alnum()        #True if only letters and numbers, not blank
spam.isdecimal()    #True if only numeric characters, not blank
spam.isspace()      #True if only spaces, tabs, newlines, not blank
spam.istitle()      #True If Each Word Starts With A Capital Letter Like This

'Hello world!'.startswith('Hello')  #---> True
'Hello world!'.endswith('world')  #---> True

', '.join(['cats', 'bats', 'rats'])  #---> 'cats, bats, rats'
' '.join(['I', 'am', 'sentient'])    #---> 'I am sentient'

'My name is REAL PERSON'.split()    #--->['My', 'name', 'is', 'REAL', 'PERSON']
'My-name-is-REAL-PERSON'.split('-') #--->['My', 'name', 'is', 'REAL', 'PERSON']


spam = '''Line one
Line two
Line three'''
spam.split('\n')    #---> ['Line one', 'Line two', 'Line three']


'Hello'.rjust(10)   #---> '     Hello'
'Hello'.rjust(20)   #---> '               Hello'
'Hello'.rjust(20,'-') #-> '---------------Hello'

'Hello'.ljust(20)   #---> 'Hello               '
'Hello'.ljust(20,'*') #-> 'Hello***************'

'Hello'.center(20)  #---> '       Hello        '
'Hello'.center(20,'=')#-> '=======Hello========'

'     Hello     '.strip()   #---> 'Hello'
'     Hello     '.rstrip()  #---> '     Hello'
'     Hello     '.lstrip()  #---> 'Hello     '


spam = 'SpamSpamBaconSpamEggsSpamSpam'
spam.strip('ampS')  #---> 'BaconSpamEggs'
#Passing in arguments to strip() will erase any instance
#of those characters off the ends of the string

import pyperclip
pyperclip.copy("Text to copy") #copies text to clipboard
pyperclip.paste()  #Returns string with whatever is copied in clipboard


#==========================================================================
#======================= Part II: Automating Tasks ========================
#==========================================================================

#--------Chapter 7: Pattern Matching with Regular Expressions--------#

import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
num = phoneNumRegex.search('My number is: 647-532-2227.')
print('Phone number found: '+ num.group())

#pass in a raw string by adding an r before string content
#phoneNumRegex now contains a Regex (pattern) object for phone #
#num will store a Match object if there's a match or None if there isn't
#group() will return the matct
#search() returns Match object
#group() returns string object

#adding parantheses in pattern makes groups
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242')
mo.group(1) #---> '415'
mo.group(2) #---> '555-4242'
mo.group(0) #---> '415-555-4242'
mo.group()  #---> '415-555-4242'

mo.groups() #---> ('415', '555-4242')
areaCode, number = mo.groups()  #Multiple assignment since groups() returns tuple

re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')  # use \( and \) as escape characters
mo.search('My number is (415) 555-4242.')  # Escape chars skip brackets in search
.group(1)   #---> '(415)'
.group(2)   #---> '555-4242'

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
