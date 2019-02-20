from functools import reduce
''' THIS IS ONLY FOR REFERENCE AND DO RUN AS IT IS. PLEASE MARK THE BLOCKS WITH
COMMENT AND UNCOMMENT TO TEST THE SAME
Day 3 , session 3----------------------------------------
---------------------------------------------------------'''

# print position and value
for position,value in enumerate(range(1,10)):print (position,value)

myList = ['f','a','s']
#always removes last element of the list 
myList.pop()
#pops item at index specified 
myList.pop(1) 
del myList[0]
#remove item by value 
myList.remove('f') 


# pack same size list or dictionary
players=['Dhoni','Rohit','Ashwin']
scores=[55,45,35]
for player,score in zip(players,scores):
    print (player,score)

#
#
# accept elements in one go
scores=eval(input('Enter Scores:'))
for score in scores: print (score)

# accept various type of data in one go as list

scores=eval(input('Enter Scores:')) #enter char value like '10 + 5 '
for score in scores:
    print (score,type(score))

#packing list
firstInnings=[1,11,21,31,41,51,61,71,81,91]
secondInnings=[9,19,29,39,49,59,69,79,89,99,191]
#firstInnings[START:END(n-1):STEP]
print(firstInnings+secondInnings)

list(zip(firstInnings,secondInnings))

# sum of both innings
for firstin,secondin in zip(firstInnings,secondInnings):
    print('Total :', firstin+secondin)

# built-in functions
firstInnings=[1,11,21,31,41,51,61,71,81,91]
print('Length: ',len(firstInnings))
print('Sum: ',sum(firstInnings))
print('Max: ',max(firstInnings))
print('Min: ',min(firstInnings))
print('Average: ',sum(firstInnings)/len(firstInnings))

# methods
score=[100,50,0,25,75]
print ('Score: ',score)
score[2]=1 # modification
print ('zero replaced with 1: ',score)
score.append(100) # append
print ('Appends at the end: ',score)
score.remove(100) # removes first matching value
print ('Removes first matching: ',score)
print ('first occurance of 100: ',score.index(100))
print ('removed value from 4th position (100): ',score.pop(4))
print ('list after removal of 100: ',score)
print ('Insert value 100 at 0th position: ',score.insert(0,100))
print ('list after inserting 100: ',score)
score.sort()
print ('list after sort :',score)
score.reverse()
print ('list after reverse sort :',score)

#accessing list elements
score=[100,50,0,25,75]
print ('print all :',score[:])
print ('print alternate items:',score[::2])
print ('print 0,1,2:',score[:3])
print ('print 4,5:',score[3:])
print ('print 1,2,3:',score[1:4])
score=[]
print ('after intialize :',score[:])
 
# if we one statement to performed in for loop
marks =[75,95,85,90,80]
GPA = [ ((mark/100)*10) for mark in marks]
print ('GPA: ',GPA)

# if we one statement to performed in for loop and also specify some condition
marks =[75,95,85,90,80]
GPA = [ ((mark/100)*10) for mark in marks if (mark>=90) ]
print ('GPA: ',GPA)

#split and join

line = 'welcome to python class to learn python basics'
words = line.split() # by default it takes space as the delimeter
print ('Input line: ',line)
for word in words: print ('line in to words...:',word)
word= [eachword.upper() for eachword in words]
newLine = ' '.join(word)
print ('Input line: ',newLine,'type',type(newLine))

# two dimensional list
scores=[[55,56,57,58,59],[65,66,67,68,69]]
print ('first row:',scores[0])
print ('Second row:',scores[1])
print ('first row first and second row second element:',scores[0][0],scores[1][1])

# building bmi table in single statement
height=[4.4,4.5,4.6,4.7,4.8,4.9,5,5.1,5.2,5.3,5.4,5.4,5.5,5.6,5.7,5.8,5.9,6,6.1,6.2]
weight=[60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98]
bmi=[[h,w,(w/(h*.304))] for h in height for w in weight]
for i in bmi:
    print (i[0],i[1],i[2])

#use of filter function with fd interest calculation
fdsName = ['Ramesh','Suresh','Magesh','Vignesh','Brijesh']
fdsAge =[54,65,72,35,55]
fdsAmt =[500000,500000,500000,500000,500000]
def fltnames(age):
    if age>=55:
        return True
#fdsAge = filter(fltnames,fdsAge)
#for i in fdsAge:print (i)

# use of map function with fd interest calculation
def calcMaturity(age,amount):
    regInt = 7/100
    ssInt = 7.5/100
    if age >= 55:
         return (amount+(amount*ssInt))
    else:
        return (amount+(amount*regInt))
matAmount=list(map(calcMaturity,fdsAge,fdsAmt))
print (matAmount)

for name,matAmt in enumerate(matAmount):
    print (fdsName[name],matAmt)

fdsName = ['Ramesh','Suresh','Magesh','Vignesh','Brijesh']
fdsAge =[54,65,72,35,55]
fdsAmt =[500000,500000,500000,500000,500000]
#alternate implementation
retamt = lambda age,amount:amount+(amount*.07) if age>54 else amount+(amount*.075)
matAmount=map(retamt,fdsAge,fdsAmt)
print (matAmount)
for name,matAmt in enumerate(matAmount):
    print (fdsName[name],matAmt)


# use of reduce function
from functools import reduce
def totMatAmt(amt,prvamt):
    return amt+prvamt

fdsAmt =[500000,500000,500000,500000,500000]
print(reduce(totMatAmt,fdsAmt))

#print the max value in the given sequence
fdsAmt =[500000,400000,340000,900000,200000]
maxAmtBetween = lambda amt,prv : amt if amt>prv else prv
maxAmt = reduce(maxAmtBetween,fdsAmt)
print (maxAmt)


 