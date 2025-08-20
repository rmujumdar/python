# ------------------------------------------------------------------------
# PYTHON BASICS - QUICK REFERENCE GUIDE
# ------------------------------------------------------------------------
# References:
# Google Scholar Tutorials: https://youtu.be/tKTZoB2Vjuk?si=DaoyTmVqe67qHNlz
# Harvard CS50 Introduction to Programming with Python: https://www.youtube.com/watch?v=nLRL_NcnK-4

print('hello world')

# ------------------------------------------------------------------------
# SIMPLE VARIABLES
# ------------------------------------------------------------------------
# Use single quotes in Python for strings
# No semi colon for line ending like in C programming
# Spacing matters

int_var = 10
float_var = 3.14
bool_var = True
null_var = None

print (int_var, float_var, bool_var, null_var, sep=', ')

# ------------------------------------------------------------------------
# SEQUENCE VARIABLES
# ------------------------------------------------------------------------
# Elements in a sequence variable is accessed via their index

string_var = 'alice'
list_var = [1,2,3,4]
tuple_var = (10.0, 20.0) # ordered, immutable. Eg: x,y cordinates
set_var = {1,2,3,4} #unordered, unique elements

print (string_var, list_var, tuple_var, set_var, sep=', ')

# ------------------------------------------------------------------------
# MAPPING VARIABLES
# ------------------------------------------------------------------------
# Elements in a mapping variable is accessed via their key

dict_var = {
  'names': ['alice','bob','christie'],
  'age': [21, 33, 42]
}
print(dict_var['names'])
print(dict_var['names'][0])

# ------------------------------------------------------------------------
# STRINGS
# ------------------------------------------------------------------------
s = 'hello'
m = '''this is a
multi-line string'''
r = r'*** Raw string with \\special// characters'

# String Concatination
sm = s + '\n' + m
print(sm)

s = "Welcome to Python Basics"
# String Length
len(s)
# String Membership
if 'Welcome' in s:
  print('Welcome!')

# String Indexing and Slicing
# Syntax: string[start:stop:step]
#
s[0] #index of first character
s[0:7] # slicing [0:n] does not include the nth charcter
s[:7] # same as s[0:7]
s[-1] # index of last character
s[-6:-1] # this not print the last character
s[-6:] # this will print the last character
s[0:10:2] # this is skip every 2nd letter
s[::2] # entire string but only every 2nd letter
s[::-1] # reverse the whole string
s[0:10:-1] # prints empty string since it's starting at index 0, and negative steps from 0 is empty
s[10:0:-1] # reverses string starting from 10th character in steps of 1

# String formatting, f-strings
name, score = 'John Doe', 90.45
f'Hi {name}, your score is {score:.1f}'

# String Case Conversion
'hello'.upper()
'HELLO'.lower()
'MiXeD cAsE'.swapcase()
'title case'.title()
'capitalize word'.capitalize()

# String Strip Whitespace and Characters
'  hi!  '.strip()
'  hi!'.lstrip()
'hi!  '.rstrip()
'**hi!**'.strip('*')

# String Search/Test
s = 'abracadabra'
s.find('br') # returns index of first occurrance
s.rfind('br') # returns index of last occurrance
s.find('xyz') # returns -1 if not found
s.index('br') # returns index of first occurance
s.index('xyz') # returns ValueError if not found
s.count('a')
s.startswith('a') # returns True
s.endswith('b') # returns False

# String Replace
'27-Aug-1988'.replace('-','/')

# String Split, Join
'A, B, C'.split(', ') # returns ['A','B','C']
'line1\nline2'.splitlines() # returns ['line1', 'line2']

",".join(['A','B','C']) # returns 'A,B,C'

# String Partition
'user@email.com'.partition('@') # returns ('user', '@', 'email.com')

# String Tests
"abc".isalpha() # True
"123".isdigit() # True
"abc123".isalnum() # True
"  \t".isspace() # True
"Title Case".istitle() # True

# ------------------------------------------------------------------------
# LISTS
# ------------------------------------------------------------------------
# Lists are Python's version of arrays
# syntax: list_var[]
list_var = [1, 2, 3]
mixed_list = [1, 'a', True, 'John Doe']

# list() to convert Range, String into a List
range_object = range(0,5) # range() returns a range object, not a list
range_list = list(range(0,5)) # use list(range_object) to convert it into a list
chars = list('abcd') # use list(string_var) to convert string into a list of char
print(range_list, chars)

# List Building
list_var = []
list_var.append(0) # add one element to the end of the list
list_var.extend(list(range(1,5))) # adds the contents of another list to the list
list_var.insert(6,'six') # inserts 'six' 6 at index 6
list_var.remove('six') # remove element by value
del list_var[0] # remove element by index
popped = list_var.pop() # remove and return the element at last index
list_var.clear()
print(list_var)

# Common List Operations
nums = [3, 1, 4, 1, 5, 9]
len(nums)
sum(nums)
min(nums)
max(nums)
nums.count(1) # counts the number of occurances of an element
nums.index(1) # index of the first occurance of an element

# List Sorting, Reverseing
nums = [3, 1, 4, 1, 5, 9]
nums.sort()
nums.sort(reverse=True)
nums.reverse()
print(nums)

# List Memebership Test
nums = [3, 1, 4, 1, 5, 9]
2 in nums # returns False
2 not in nums # returns True

# List Comprehension
squares = [x**2 for x in range(5)]
print(squares)
evens = [x for x in range(10) if x%2==0]
print(evens)

# Copying List
# using b = a points to the same list
a = list(range(5))
b = a.copy()
b = list(a)
b = a[:] # copy using slice
b.reverse()
print(a, b)

# 2x2 Matrix List
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[0][0])

# ------------------------------------------------------------------------
# TUPLES
# ------------------------------------------------------------------------
# immutable
# for fixed data that you don't want to be modified
# only elements of a list within tuples can be modifed
# Tuples can be used as keys in a dictionary, unlike lists

empty_tuple = ()
single_tuple = (5,) # need a ,
normal_tuple = ('John Doe', '39', ['jdoe@email.com', 'john_doe@workmail.com'])
print(normal_tuple[0])
normal_tuple[0] = 'Jane Doe' # leads to a Type Error
normal_tuple[2][0] = 'newemail@email.com' # list item within tuples can be modified
print(normal_tuple)

# Tuple Unpacking
point = (3,4)
x,y = point
print(x,y)
# Tuple Extended Unpacking
numbers = (1, 2, 3, 4, 5)
a, *b, c = numbers
print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  # 5

# Tuple Useful operations
numbers = (1, 2, 3, 4, 5, 2, 2)
len(numbers)
numbers.count(2)
numbers.index(2)
9 in numbers
9 not in numbers

# ------------------------------------------------------------------------
# DICTIONARY
# ------------------------------------------------------------------------
# A map of key:value pairs
# Keys must be unique
# Dictonary items are accessed via keys, not index

person = {
  'name': 'John Doe',
  'age': 39,
  'email': ['jdoe@email.com', 'john_doe@workmail.com']
}
print(person['email'])

# Creating dictionary using dict()
person = dict(name='John Doe', age=39, email=['jdoe@email.com', 'john_doe@workmail.com'])
print(person['email'])

# Updating dict values
person['age'] = 40
print(person['age'])

# Removing dict values
person.pop('age') # removes key:value pair using the specified key
del person['age'] # removes key:value pair using the specified key
person.popitem() # removes the last inerted itme
person.clear() # empties the dictionary
print(person)

# Checking Membership
person = {
  'name': 'John Doe',
  'age': 39,
  'email': ['jdoe@email.com', 'john_doe@workmail.com']
}
'name' in person # True. checks keys, not values
'John Doe' in person # False. checks keys, not values

# Dictionary Comprehension
squares = {x:x**2 for x in range(5)}
print(squares)

# Nested Dictionaries
students = {
  's1': {'name':'Jane Doe', 'age':20, 'gender':'female'},
  's2': {'name':'James Dune', 'age':21, 'gender':'male'}
}
students['s1']['name']

# Dictionary Methods
students.keys()
students.values()
students.items()



# ------------------------------------------------------------------------
# CONDITIONAL STATEMENTS
# ------------------------------------------------------------------------
test_var = -10
if test_var > 0:
  print('Positive')
elif test_var == 0:
  print('Zero')
else:
  print('Negative')

# if in
if 'a' in 'abc':
  print('ayy!')

# Ternary Conditional Expression, i.e. one-line if/else
age = 20
status = 'adult' if age>=18 else 'minor'
print(status)

# ------------------------------------------------------------------------
# LOOPING STATEMENTS
# ------------------------------------------------------------------------

# For loop
list_var = [0,1,2,3,4,5]
for i in list_var:
  print(list_var[i])

# For loop with range()
# note that range() does not include that end number
for i in range(0,6):
  print(i)

# While loop
i = 0
while i<=5:
  print(i)
  i += 1

# For loop with break
for i in range(10):
  print(i)
  if i == 3:
    break # exit loop if condition is met

# For loop with continue
for i in range(10):
  if i in [3,6,9]:
    continue # skips this iteration
  print(i)

# For Else loop
for i in range(6):
  print(i)
else:
  print("Loop finished!")

# ------------------------------------------------------------------------
# FUNCTIONS
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# FILES
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# REGULAR EXPRESIONS
# ------------------------------------------------------------------------