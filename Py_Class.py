 # -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 16:33:52 2017

@author: IOA
"""

x = "First # String"
x.upper()
x.split("#")
x.split("#")[-1]

list_one = [10,11,12]
list_pop = list_one.pop()   #remove last element
print(list_pop)

list_one = [10,11,12,13]
list_pop_ind = list_one.pop(0) # pop by index
print(list_pop_ind)

# default(implicit) order
default_order = "{}, {} and {}".format('John','Bill','Sean')
print('\n--- Default Order ---')
print(default_order)

# order using positional argument
positional_order = "{1}, {0} and {2}".format('John','Bill','Sean')
print('\n--- Positional Order ---')
print(positional_order)

# order using keyword argument
keyword_order = "{s}, {b} and {j}".format(j='John',b='Bill',s='Sean')
print('\n--- Keyword Order ---')
print(keyword_order)


for m in range(10,0,-3):
    print(m)
#map, filter 
items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)
    
items = [1, 2, 3, 4, 5]
#map function applies a passed-in function to each item in an iterable object and returns a list 
squared = list(map(lambda x: x**2, items))

squared1 = map(lambda x: x**2, items) # error

print(squared)

def multiply(x):
    return (x*x)
def add(x):
    return (x+x)
#lambda
funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)

#another example for map
pow(5,10)
pow(6,7)
pow(3,4)

list(map(pow, [5, 6, 3], [10,7, 4]))
#map example3
x = [11,22,23]
y = [40,50,60]

from operator import add
print (list(map(add, x, y)))


from itertools import zip_longest # zip_longest() makes an iterator that aggregates elements from the two iterables
for i,j in zip_longest(x,y):
    print(i,j)

number_list = range(-5, 5)

#filter extracts each element in the sequence for which the function returns True. 
#filter ex 1
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

# same as filter ex1
result = []
for x in range(-5, 5):
	if x < 0:
		result.append(x)

result

#filter ex2
a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]
print (list(filter(lambda x: x in a, b) ))
#same as above filter stmt
print ([x for x in a if x in b] )

#reduce
#reduce is in the functools in Python 3.0. 
#It is more complex. It accepts an iterator to process, 
#but it's not an iterator itself. It returns a single result:

from functools import reduce
reduce( (lambda x, y: x * y), [1, 2, 3, 4] )

#same code for above reduce
L = [1, 2, 3, 4]
res = L[0]
for x in L[1:]:
    res = res * x
res


#for else
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'is not a prime number')
            break
        
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print( n, 'is not a prime number')
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
        
#Collections
from collections import defaultdict

colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

favourite_colours = defaultdict(list)


for name, colour in colours:
    favourite_colours[name].append(colour)

print(favourite_colours)

# A simple example class
class Test:
     
    # A sample method 
    def fun(self):
        print("Hello")
 
# Driver code
obj = Test()
obj.fun()

obj.fun("Python") #error


# A Sample class with init method
class Person:
 
    # init method or constructor
    #self is an instance of a method in the class
    
    def __init__(self, name):
        self.name = name
        
       # print(name)
 
    # Sample Method 
    def say_hi(self):
        print('Hello, my name is', name)

        
p1 = Person() #error
p = Person('Venkat ')
p.say_hi()

p1 = Person('Chandini ')
p1.say_hi()

p2 = Person('Vishnu ')
p2.say_hi()

p3 = Person() # error


# Class for Computer Science Student
class CSStudent:
 
    # Class Variable
    stream = 'cse'            
 
    # The init method or constructor
    def __init__(self, roll):
   
        # Instance Variable    
        self.roll = roll       
  
# Objects of CSStudent class
a = CSStudent(101)
b = CSStudent(102)
  
print(a.stream)  # prints "cse"
print(b.stream)  # prints "cse"
print(a.roll)    # prints 101
  
# Class variables can be accessed using class
# name also
print(CSStudent.stream) # prints "cse"  


#We can define instance variables inside normal methods also.

# Python program to show that we can create 
# instance variables inside methods
  
# Class for Computer Science Student
class CSStudent:
     
    # Class Variable
    stream = 'cse'     
     
    # The init method or constructor
    def __init__(self, roll):
         
        # Instance Variable
        self.roll = roll            
 
    # Adds an instance variable 
    def setAddress(self, address):
        print(self.roll)
        self.address = address
     
    # Retrieves instance variable    
    def getAddress(self):    
        return self.address   
 
# Driver Code
a = CSStudent([101,102,103])
a.setAddress("Noida, UP")
print(a.getAddress()) 


arr = [1,2,5]


#class example
class Car(object):
	"""
		blueprint for car
	"""

	def __init__(self, model, color, company, speed_limit):
		self.color = color
		self.company = company
		self.speed_limit = speed_limit
		self.model = model

	def start(self):
		print("started")

	def stop(self):
		print("stopped")

	def accelarate(self):
		print("accelarating...")
		"accelarator functionality here"

	def change_gear(self, gear_type):
		print("gear changed")
		" gear related functionality here"
  

maruthi_suzuki = Car("ertiga", "black", "suzuki", 60)
audi = Car("A6", "red", "audi", 80)

audi.accelarate()
audi.change_gear(4)
print(audi.color)
print(maruthi_suzuki.company)

#class example 2
class Rectangle:
   def __init__(self, length, breadth, unit_cost=0):
       self.length = length
       self.breadth = breadth
       self.unit_cost = unit_cost
   
   def get_perimeter(self):
       return 2 * (self.length + self.breadth)
   
   def get_area(self):
       return self.length * self.breadth
   
   def calculate_cost(self):
       area = self.get_area()
       return area * self.unit_cost
# breadth = 120 cm, length = 160 cm, 1 cm^2 = Rs 2000
r = Rectangle(160, 120, 2000)
print("Area of Rectangle: %s cm^2" % (r.get_area()))

print(r.calculate_cost())
print("Cost of rectangular field: Rs. %s " % (r.calculate_cost()))



import pdb

def make_bread():
    pdb.set_trace()
    for x in range(2,10):
        #pdb.set_trace()
        x = x+2
        print(x)
    
    return "trace not needed"

#c: continue execution
#w: shows the context of the current line it is executing.
#a: print the argument list of the current function
#s: Execute the current line and stop at the first possible occasion.
#n: Continue execution until the next line in the current function
#is reached or it returns.
print(make_bread())


import pdb, traceback, sys

def bombs():
    a = []
    print (a[0])

if __name__ == '__main__':
    try:
        bombs()
    except:
        type, value, tb = sys.exc_info()
        traceback.print_exc()
        pdb.post_mortem(tb)