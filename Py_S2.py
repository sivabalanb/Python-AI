''' THIS IS ONLY FOR REFERENCE AND DO RUN AS IT IS. PLEASE MARK THE BLOCKS WITH
COMMENT AND UNCOMMENT TO TEST THE SAME
'''
# comments
# wokring with numbers - int and float (long and complex not used much)

# working with strings - [start:end:steps], start postion, end no of chars
string='123456789'
string[:] # will print all characters
string[2:] # from 3rd postion
string[:2] # from 0 to 2-1 postion
string[2:4] # from 2 to 4-1 postion
string[0:4] # from 0 to 4-1 postion
string[0:9] # all
string[0:9:3] # jump in 3 steps
string[9:0:-1] # negetive sequence
string[::-1] # negetive sequence


# program to find the weight in pounds by accepting kgs
Weight=int(input('Enter weight in Kgs:')) #input is alwasy string
print ('Weight in Pounds:',Weight*2.2)

print('India increased their medal tally to \
25 in 18th asian games') # \ used to terminate the line

print (weight) # will fail due case senstivity

# calculator program, eval
Total=eval(input('Enter your calculations:'))
print ('Total = :',Total)

#print name in two lines, understand \n and sep
fname='Rohit'
lname='Sharma'
print(fname,lname)
print(fname,'\n',lname)
print(fname,'\n',lname,sep='...')


# bmi calculator, intro to if statement
Weight=int(input('Enter weight in Kgs:')) #input is alwasy string
Height=float(input('Enter height in feet:')) # float outcome
#Height=eval(input('Enter height in feet:')) # will handle both

bmi=Weight/((Height*.304)**2) # formula is W/M^2
if bmi > 24.9: # if statement :
    bmiIndicator = 'Above Normal'
    bmiStat=3
elif bmi < 18.5:        # else if
    bmiIndicator = 'Below Normal'
    bmiStat=2
else:
    bmiIndicator='Normal'
    bmiStat=1
print ('BMI is ',bmiIndicator,' value is ',bmi) # handling decimals will be later

# heart rate status finder
heartRate=eval(input('Enter your heart rate: '))
if heartRate > 100: # if statement :
    heartIndicator = 'Above Normal'
    heartStat=3
elif heartRate < 60: # else if
    heartIndicator = 'Below Normal'
    heartStat=2
else:
    heartIndicator = 'Normal'
    heartStat=1
print ('heartRate is',heartIndicator,'value is ',heartRate)

# health status checking
if (bmiStat,heartStat) == (1,1): # compare two values at a time
    healthIndicator='Normal'
else:
    healthIndicator='Do More exercise and workouts!!!'

print ('Your Health status:',healthIndicator)

# for loops
#for i in 1,10:print (i) # print each as element
for i in range(1,10):print (i) # print 1 to 9, loops break
for i in range(1,10,2):print (i) # print 1 to 9, jump 2 steps
for i in range(10,1,-2):print (i) # print 10 to 1, jump 2 steps
for i in range(10,1,-1):print (i) # print 10 to 1, jump 1 steps

sentence='Welcome to Python' # for loop for strings
for char in sentence:print (char) # char per line
for char in sentence:print (char,end='') # end will supress the new line

#for loop for list
Scores=[11,21,31,41,51,61,71,81,91,101] # for loop for list
for score in (Scores): print (score)

#for loop for tuple
scores=('dhone',45,55)
print (type(scores)) # to get the type of the object
for score in scores:print (score)

#for loop for dictionary
age={'Dhone':35,'Rohit':30,'Ashwin':29}
for player in age:print (player) # print the key
for player in age:print (player,age[player]) # print both key and value

#for with break
orders=[1,2,3,4,5,6,7,8,9,10]
for order in orders:
    print (order)
    if order == 3:
        break
   
#for with continue
orders=[1,2,3,4,5,6,7,8,9,10]
for order in orders:
    if order == 3:
        continue
    print (order)

# while loop
printmyname='Y'
while (printmyname in ('Y?y')): # check the usage of in
    print ('Hello')
    printmyname = input('Do you want to continue...Enter Y or N')

#defining functions
# finonnaci = 0+1+1+2+3+5+8+13...
def fibonnaci(getnum): # defining function and passing arguments
    prev=0
    curr=1
    while (curr<getnum):
        #print (curr)
        print (curr)
        prev=curr
        curr=curr+prev
      
        
fibonnaci(5) # calling function

#default values
# bmi calculator as function and with default values
def find_bmi(Weight=100,Height=6):
    bmi=Weight/((Height*.304)**2) # formula is W/M^2
    if bmi > 24.9: # if statement :
        bmiIndicator = 'Above Normal'
        bmiStat=3
    elif bmi < 18.5:        # else if
        bmiIndicator = 'Below Normal'
        bmiStat=2
    else:
        bmiIndicator='Normal'
        bmiStat=1
    return ('BMI is ',bmiIndicator,' value is ',bmi) # return value

#print ("both given",find_bmi(79,5.6)) # call one
#print ("only weight",find_bmi(79)) # call with only weight, height=6
#print ("none",find_bmi()) # call with only weight, height=6
print (find_bmi(Height=5,Weight=200)) # keyword arguments

#lambda expression
#lambda expression , sum of two numbers
sum = lambda num1,num2:num1+num2
print (sum(5,5))

#Celsius to Fahrenheit 
tempinfarenheit = lambda num:(num*1.8)+32
print (tempinfarenheit(32))

#find the factorial using recursive function
def factorial(getnum):
    if getnum == 1:
        return 1
    print (getnum)
    return (getnum*factorial(getnum-1))
print (factorial(5))

# fib from to bottom
def fibrecur(getnum):
    if (getnum <=1 ):
        return 1
    print (getnum)
    return getnum+(fibrecur(getnum-1))
print (fibrecur(5))

#for loop for dictionary
scores=[{'Dhone':(35,45)},{'Rohit':(30,40)},{'Ashwin':(29,50)}]
for score in scores:
    aa=score
    for jj in aa:print (jj,aa[jj][0],aa[jj][1])
    #print (aa)
    #print (score[0]) # print the key

'''
