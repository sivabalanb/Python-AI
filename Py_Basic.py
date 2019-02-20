# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 10:38:50 2017

@author: IOA
"""

# -*- coding: utf-8 -*-

#Spyder Editor

v = 30
a = (40)
print(v)

x, y = 10,'20'

V = input("Enter value for V1")

V1 = int(input("Enter value for V1"))

print(V1)
type(V1) #type of the object
type(Vv1)
 



#Assigning Values to Variables
counter = 100 # An integer assignment
miles = 1000.0 # A floating point
name = "John" # A string
print (counter)
print (miles)
print (name)

#Multiple Assignment
a = b = c = 1

a,b, c = 1, 2, "john"

#Pyth on has five standard data types- Numbers,  String,  List,  Tuple,  Dictionary

var1 = 1
var2 = 10

del var1 # to delete the varaiable/object

#Python strings
str = 'Hello World!'
print (str) # Prints complete string
print (str[0]) # Prints first character of the string
print (str[2:5]) # Prints characters starting from 3rd to 5th
print (str[2:]) # Prints string starting from 3rd character
print (str * 2) # Prints string two times
print (str + "TEST") # Prints concatenated string



#input
name = input("Please enter your name:") #The type of value read by Python is always a string.
print("The name you entered was", name)
type(name)

age = int(input("Please enter your age:"))
olderAge = age + 1
print("Next year you will be", olderAge)

#formating output
name1 = "ABC"
print(name1,"how are you doing?")
print("I hope that,", name1, "is feeling well today.")

base = float(input("Please enter a number: "))
exp = float(input("Please enter an exponent: "))
answer = base ** exp
print(str(base) + "^" + str(exp), "=", answer)
 
print(base , "^" , exp, "=", answer)
m1 = 1000

m2 = 250
print(m1+m2)

print((1,2)+(3,4))

names = "{1}, {2} and {0}".format('John', 'Bill', 'Sean')
print(names)





#Python List
list1 = [ 'abcd', 786 , 2.23, 'john', 70.2 ,786]
tinylist = [123, 'john']

print (list1) 			# Prints complete list
print (list1[0]) 
print(list1[-1])			# Prints first element of the list
print (list1[0:5])			# Prints elements starting from 2nd till 3rd 
print (list1[:2])			# Prints elements starting from 3rd element
print (tinylist * 2) 			# Prints list two times
print(tinylist[0]*2)
print(tinylist[1]*2)
print (list1 + tinylist) 	

#This is a temporary script file.
list1+[987]

list1+'0987'

list1.append(988)

count(list1) #error
list1.count(988)
list1.count(786)

import Panda_simple_data.py
import session2 as s
s.fibonnaci(5)

type(list1)
list1.__class__

print(len(list1))

print(78 in list1)

print(786 in list1)

print(list1.count(786))
print(list1[1])


8 in [5,8,7,12]

list1[1] = 1000
print(list1)
list1[6] = 22
list1.append(22)
#list2 = list()

#print(list2)

t = (345,"aaa")

t1 = [345,'aaa']
print(t)

em = ()
em1 = []
emd ={}

t[1] = "bbb" #tuple cannot be updated
t1[1]= "ccc"
#to update tuple
t2 = list(t)
t2[1] = "bbb"


aList = [123, 'xyz', 'zara', 'abc']

aT = (123, 'xyz', 'zara', 'abc')

aList[0] = 456
aTuple = tuple(aList) #tuple - read only list
aTuple[0] = 123
print(type(aList))
print(type(aTuple))


type(list1)

list1.__class__

blist = list(aTuple)
print(blist)


print ("Tuple elements : ", aTuple)

#set
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)   

'orange' in basket                 
'crabgrass' in basket
                   

dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
dog = dogs[0]

print(dogs[0])
print(dog.title())

dog = dogs[1]
print(dog.title())

dog = dogs[-1]
print(dog.title())

dog = dogs[-2]
print(dog.title())

dog = dogs[-4]
print(dog.title())

#More list operations
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')

fruits[:-4]

for i in list1:
    print(i*3)
 
for x in fruits:
    print(x)
    
total = 0; # This is global variable. 
# Function definition is here 

def sum( arg1, arg2 ): 
   # Add both the parameters and return them." 
   total = arg1 + arg2; # Here total is local variable. 
   print ("Inside the function local total : ", total )
   return total; 
 
# Now you can call sum function 
sum( 10, 20 ) 
print ("Outside the function global total : ", total )

#dictionaries
# empty dictionary
my_dict = {}

# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}

# dictionary with mixed keys
my_dict = {'name': 'Shan', 1: [2, 4, 3]}

# using dict()
my_dict = dict({1:'apple', 2:'ball'})

# from sequence having each item as a pair
my_dict = dict([(1,('apple','india','America')), (2,'ball')])

my_dict1 = dict(((1,'apple'), (2,'ball')))

my_dict1 = dict((1,'apple'), (2,'ball')) #error


tinydict = {'name': 'john','code':6734, 'dept': 'sales'} 

dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}
print ("dict['Name']: ", dict['Name'])


print (tinydict) 			# Prints complete dictionary 
print (tinydict.keys()) 			# Prints all the keys 
print (tinydict.values() )
print(tinydict.items())
print(tinydict['code'])
tinydict['code'] = 2456
tinydict['City'] ='Chennai'

dict = {} 
dict['one'] = "This is one" 
print(dict)
dict[2] = "This is two" 
print(dict)
dict[3]= 123
print(dict)
dict[3]= 789
print (dict['one']) 		# Prints value for 'one' key 
print (dict[2] )			# Prints value for 2 key 
lis = []
lis[1] = 200

lis.append(200)
print(lis[0])
d1 = {}
d1[1] = "a"
#print(d1)
d1[2] = 98
#print(d1)
d1[3] = "xxx"
#del d1
print(d1)




squares = {1:1, 2:4, 3:9, 4:16, 5:25}  

print(squares.pop(4))  
print(squares)


a = 10
print(a)
x,y,p = 20,'3',45
print(x,y)

tup = ("rabbit", "mouse", "gorilla", "giraffe")
print(tup)
# Join tuple with no space.
s = "".join(tup)
print(s)

# Join tuple with slash.
s = "/".join(tup)
print(s)

vehicles = ["car", "truck", "tractor"]

# Convert list to string with join.
result = "".join(vehicles)

# Convert with semicolons separating strings.
result2 = ";".join(vehicles)

print(result)
print(result2)

# Convert dictionary to list of tuples.
items = list(tinydict.items())
print(items)

for item in items:
    print(len(item), item)
    
#dict to other types
vegetables = {"carrot": 1, "squash": 2, "onion": 4}

print(vegetables.keys())

vehicles = ["car", "truck", "tractor"]
print(len(vehicles))

for b in [1,4,12,23,90]:
    print(b)
    print(b+1)
    print(b*2)
    
for x in (10,20,12,35,46,67):
    print(x)

for x in vegetables.items():
    print(x)

for x in [10,20,30,100]:
    print(x)
    

vegetables = ("carrot", "squash", "onion")

# Convert to list.
veg2 = list(vegetables)

veg2.append("lettuce")
print(veg2)


Pyth = "string"

word = ['p','y','t','h','o','n']

import fibo as f

dir(f)
import fibo
f.fib(27)

fibo.fib(15)
fibo.fib2(10)
f.name1(50)

lst = [1,2,[3,4],[5,[100,200,["Hello"]],23,11],1,7]
len(lst)
lst[3][1][2]
lst[3][1][2]

d = {'k1': [1,2,3,{'tricky':['one', 'two', 'between', {'target': [4,5,6,'hello']}]}]}




d['k1'][3]['tricky'][3]['target'][3]



d['k1'][3]['tricky'][3]['target'][3]

stn = "sample@domain.com"



ss = stn.split('@')

import string

stng = "This ice bird fly faster than other normal bird"


for w in stng.lower().split():
        print(w)
print(type(w))
print(len(w))
       
s1 = stng.lower().split() 
type(s1)
print(s1[0])
len(s1)
d = []
i = 0
stng = "This ice bird # fly faster than other normal Bird"
s1 = stng.lower().split() 

for w in s1:
    if w == 'bird':
        d.append(0)
    elif w == "bird" and w[i+1].isdigit()== "True":
        d.append(0)
    elif w == "bird" and w[i+1] == "#":
        d.append(0)
    else: 
        d.append(1)
   # print(w[i])
    print(d[i])
    i = i+1

       
def count_bird(st):
    c =0
    for w in st.lower().split():
        if w == 'bird':
            c =  c+1
    return(c)        
            
count_bird(stng)

print(stng.lower().count('bird'))

import numpy
# x is your dataset
x = numpy.random.rand(100, 5)
numpy.random.shuffle(x)
training, test = x[:80,:], x[80:,:]

	


import numpy as np
# x is your dataset
x = numpy.random.rand(100, 5)
numpy.random.shuffle(x)
training, test = x[:80,:], x[80:,:]


# x is your dataset
x = numpy.random.rand(100, 5)
indices = numpy.random.permutation(x.shape[0])
training_idx, test_idx = indices[:80], indices[80:]
training, test = x[training_idx,:], x[test_idx,:]

import pandas as pd
dff = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
                              'foo', 'bar', 'foo', 'foo'],
                       'B' : ['one', 'one', 'two', 'three',
                              'two', 'two', 'one', 'three'],
                       'C' : np.random.randn(8), 'D' : np.random.randn(8)})

np.array_split(dff, 3)


from ipyleaflet import Map

Map(center=[34.6252978589571, -77.34580993652344], zoom=10)

import ipyleaflet
