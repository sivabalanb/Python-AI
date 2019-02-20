 # -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 17:53:23 2017

@author: IOA
"""
#Functions
#Function inside function - ex 1
def func_m():
    print('func()')
    def func1():
        print('func1')
        def func2():
            print('func2')
        func2()
    func1()
    
func_m()   
f_call = func_m
type(f_call)

f_call()

#Ex 2
def intersect(seq1, seq2):
	res = []			# Start empty
	for x in seq1:			# Scan seq1
		if x in seq2:		# Common item?
			res.append(x)	# Add to the end
	return res

intersect() # error

intersect([1, 2, 3],(1, 4,2))


x = intersect([1, 2, 3],(1, 4,2))
x 

x1 = intersect(1, 4) #Error , mismatch in data types

s1 = "WORLD"
s2 = "WORDS"

intersect(s1, s2)

[x for x in s1 if x in s2]  #replcement for the above function Ex2

#Argument Matching
def f(a, b, c):
	print(a, b, c)
 
f(1, 2, 3)

f(9,8) #error

f(c=13, b=12, a=1)

f(1, c=3, b=2)

f(m=1,n=3,p=2)  # error 

m= 10
n=20
p=30
f(m,n,p)

f(10,20,30,40) # error
f() #error

'''func(value) -	Normal argument: matched by position
func(name=value)-	Keyword argument: matched by name
func(*sequence)	-	Pass all object in sequence as individual positional arguments
func(**dict)	-	Pass all key/value pairs in dict as individual keyword arguments
def func(name)	-	Normal argument: matched any passed value by position or name
def func(name=value)	-	Default argument value, if not passed in the call
def func(*name)	-Matches and collects remaining positional arguments in a tuple
def func(**name)	-	Matches and collects remaining keyword arguments in a dictionary
def func(*args, name)	-	Arguments that must be passed by keyword only in calls'''


def f1(*args):
    	print(args)
 
f1()
f1(10,20)
f1(10,200,30)
f1(40)

def ff(x,y):
    print(x)

ff()
ff(10)
ff(10,20)


def print_all(*args):
	for x in enumerate(args):
		print( x)
  
print_all('A','b','b','a')

print_all([1,2,3],[4,5,6])

for x1 in enumerate([4,5,6]):
		print( x1)
  
def ff2(*args):
	print(args)
 
ff2()
ff2(20) # to be checked for , 
ff2(50,60,70)

args1 = (10, 20)
ff2(args1)
args1 += ((30, 40, 50))
ff2(args1)


def f1(**kwargs):
	print(kwargs)

f1()
f1(a=10, b=20)
f1(60,80) # error

def kwargs_function(**kwargs):
	for k,v in kwargs.items():
		print (k,v)

kwargs_function(**{'O':'one','T':'two','TH':'three'})

kwargs_function(t='two', th='three', o='one')

f1(t='two', th='three', o='one')

def f2(a, b, c, d, e):
	print(a, b, c, d, e)
 
f2(*args1) #unpacking arguments
args2 = [90,80]
f2(*args2) #error 

kwargs1 = {'a':10, 'b':20, 'c':30}
f2(**kwargs1)
kwargs1['d']=40
kwargs1['e']=50
f2(**kwargs1)

f2(*(10, 20), **{'d':40, 'e':50, 'c':30})
f2(10, *(20, 30), **{'d':40, 'e':50})
f2(10, c = 30, *(20,), **{'d':40, 'e':50})
f2(10, *(20,30), d=40, e=50)
f2(10, *(20,), c=30, **{'d':40, 'e':50})


def fnc(*args, **kwargs):
   print('{} {}'.format(args, kwargs))

print('fnc()')
fnc()
fnc(1,2,3)
fnc(1,2,3,'flask')
fnc(a=1, b=2, c=3)
fnc(a=1, b=2, c=3, d='ansible')
fnc(1, 2, 3, a=1, b=2, c=3)

lst = [1,2,3]
tpl = (4,5,6)
dct = {'a':7, 'b':8, 'c':9}

fnc(*lst, **dct)
fnc(*tpl, **dct)

fnc(1,2,*lst)
fnc(1,2,*tpl)
fnc('jupyter',**dct)
fnc(arg='django',**dct)
fnc(1,2,*tpl,q='bottle',**dct)


def fnc2(arg1, arg2, *args, **kwargs):
   print('{} {} {} {}'.format(arg1, arg2, args, kwargs))

print('fnc2()')
fnc2() # error
fnc2(1,2)
fnc2(1,2,3,'haystack')
fnc2(arg1=1, arg2=2, c=3)
fnc2(arg1=1, arg2=2, c=3, d='Spark')
fnc2(1,2,3, a=1, b=2)
fnc2(*lst, **dct)
fnc2(*tpl, **dct)
fnc2(1,2,*tpl)
fnc2(1,*tpl,d='nltk')
fnc2(1,2,*tpl,d='scikit')


#Arbitrary function

def A_function(f4, *args, **kwargs):
	return ff(*args, **kwargs)
 
def ff(a, b, c, d, e):
	return a*b*c*d*e
 
print(A_function(f, 10, 20, c=30, d=40, e=50))

ff(1,3,4,5,6)
