# Python Interview Questions Revision:
#2. Decorator:
# Method-1 : 
def decorator_func(func):
    def wrapper_func():
        print("Wrapper_func Worked")
        return func()
    print("decorator_func worked")
    return wrapper_func

# def show():
#     print("Show Worked")
# decorator_show = decorator_func(show)
# decorator_show()

 # Alternative Method
@decorator_func
def display():
    print('display worked')
display()

print()

# Method-2 :
import time

def greet(func):
    def inner():
        a = time.time()
        print("******")
        func()
        print("******")
        b= time.time()
        print(b-a)
    return inner
        
@greet
def addd():
    x,y = 5,4
    print(f"sum of {x} and {y} is {x+y}")
addd()

print()

@greet
def my():
    print("Ye mera hai")
my()

# List comprehension:
 # common way:
l1 = []
for i in range(10):
    if i%2:
        l1.append(i)
print(l1)

 # comprehension way:
ls = [i for i in range(10) if i%2]
print(ls)
 
# Dict Comprehension:
 # common way:
d = {}
for i in range(1,10):
    sqr = i*i
    d[i] = i*i
print(d)

 # compare way:
d1 = {n:n*n for n in range(1,10)}
print(d1)
print()

# Generator:
def sqr(n):
    for i in range(1,n+1):
        yield i*i
a = sqr(3)
print(next(a)) #1
print(next(a)) #2
print(next(a)) #9

print()

# Iterator:
iter_list = iter(['A', 'B', 'C'])
print(next(iter_list)) #A
print(next(iter_list)) #B
print(next(iter_list)) #C

# __init__.py and __init__()

class Person:
    def __init__(self, name):
        self.name = name
    
    def say_hi(self):
        print('Hello, my name is', self.name)

p = Person('Nitin')
p.say_hi()

# Module: import numpy
# Package: from my_package.abc import a



# Ternary Statement:
# [if_true] if [expression] else [if_false]

age = 25
discount = 5 if age<65 else 10
print(discount)

print()
  
# Inheritance:
class A:
    def display(self):
        print("A Display")

class B(A):
    def show(self):
        print("B show")
d = B()
d.show()
d.display()

# Break:
for i in range(10):
    if i ==7:
        break
    print(i, end=",")

print()

# Continue:
for i in range(10):
    if i == 7:
        continue
    print(i, end = ',')

print()

# Pass:
def my_fun():
    print("Pass inside function")
    pass
my_fun()

print()

# Pickling: pickle.dump(), serialization
# Unpickling: pickle.load(), deserialization

# Methods and Functions in Datatype:

# Function of list:
# sort(), append(), extend(), index(), max(list), min(list)
# len(list), list(seq), type(list)

# Function of Tuple:
# len(), max(), min(), tuple(seq), sum(), any(), all(), 
# sorted(), index(), count()

# Function of Dictionary:
# clear(), copy(), fromkeys(), get(), items(), keys(), pop(), 
# popitem(), setdefault(), exist, update(), values()

# Function of Set:
# add(), clear(), copy(), difference(), difference_update(), discard(),
# intersection(), intersection_update(), isdisjoint(), issubset(), isuperset(),
# pop(), remove(), symmetric_difference(), symmentric_difference_update(), union(), update()

print()

# Type Conversion:
# ord(): return integer of Unicode;
a = 'A'
d = ord(a)
print(d)
print(type(d))

print()

# eval(): Parses the expression argument and evaluates
a = '100+20+30'
d = eval(a)
print(d)
print(type(d))  

print()

# repr(): Return the string representation of value pass to eval fun. by default.
a = 100
d = repr(a)
print(d)
print(type(d))


print()

# *args and **kwargs:
def sum(*args):
    total = 0 
    for a in args:
        total = total + a
    print(total)
sum(1,2,3,4,5)

def show(**kwargs):
    print(kwargs)

show(A=1,C=3,E=5)

print()

# Open and With statement:
f = open("Revision_Work\myfile.txt")
content = f.read()
print(content)
f.close()

with open ("Revision_Work\myfile.txt") as f:
    content = f.read()
    print(content)

print()

# Text mode: 't'
# Exclusive creation: 'x'
# Binary mode: 'b'


# PYTHONPATH: It is an environment variable which you acan set to add additional directories 
# where python will look for modules and packages.


# Exception Handling:
# try:
#     # Some Code
# except:
#     #
# else:
#     #
# finally:
#     #


# Pyhton2.0 vs Python3.0:


# pip in Python:
# pip install <package_name>


# How to get List of all keys in a Dictionary?
# Method-1,2: Using List
dct = {'A':1, 'B':2, 'C':3}
all_keys = list(dct.keys())
print(all_keys)

# shortcut
dct = {'A':1, 'B':2, 'C':3}
all_keys = list(dct)
print(all_keys)

print()

# Method-3,4: Using Iterable Unpacking Operator:
d = {'A':1, 'B':2, 'C':3}
x = [*d.keys()]
print(x)

# shortcut
d = {'A':1, 'B':2, 'C':3}
x = [*d]
print(x)

print()

# Method-5:
# Keys() function:
d = {'A':1, 'B':2, 'C':3}
x = d.keys()
print([k for k in x])

print()

# Method-6,7:
d = {'A':1, 'B':2, 'C':3}
*x, = d.keys()
print(x)

# shortcut
d = {'A':1, 'B':2, 'C':3}
*x, = d
print(x)

print()

##### Next File 1_1 #####