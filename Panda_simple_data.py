 # -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 11:21:14 2016

@author: IOA
"""

# General syntax to import specific functions in a library: 
##from (library) import (specific library function)
#from pandas import DataFrame, read_csv

# General syntax to import a library but no functions: 
##import (library) as (give the library a nickname/alias)
import matplotlib.pyplot as plt
from numpy import random
import pandas as pd #this is how I usually import pandas
import numpy as np
import sys #only needed to determine Python version number
import matplotlib #only needed to determine Matplotlib version number
#%matplotlib inline
import os
import timeit


dir(pd)

content = dir(np)  # get methods of the package
print(content)

#

data = {'color' : ['blue','green','yellow','red','white'], 
	'object' : ['ball','pen','pencil','paper','mug'],
	'price' : [1.2,1.0,0.6,0.9,1.7]}
type(data['color'])

frame = pd.DataFrame(data)
print(data)
print(frame)


# The inital set of baby names and bith rates
names = ['Bob','Jessica','Mary','John','Mel']
births = [968, 155, 77, 578, 973]

print(names)

BabyDataSet = list(zip(names,births))
BabyDataSet


df = pd.DataFrame(data = BabyDataSet, columns=['BabyNames', 'Births'])
df


df.to_csv('births1880.csv',index=False,header=False)
# r before the string. Since the slashes are special characters, 
#prefixing the string with a r will escape the whole string.
Location = r'births1880.csv' 

os.getcwd()
#default header
df = pd.read_csv(Location)
df
#Null header
df1 = pd.read_csv(Location, header=None)
df1
#Col names
df2 = pd.read_csv(Location, names=['Names','Births'])
df2

# Check data type of the columns
df2.dtypes
type(df)
# Check data type of Births column
df2.Births.dtype

#Analyze data
# Method 1:
Sorted = df2.sort_values(['Births'], ascending=False)
Sorted
Sorted.head(3)

# Method 2:
df['Births'].max()

#Present data
# Create graph
df['Births'].plot()

# Maximum value in the data set
MaxValue = df['Births'].max()
print(MaxValue)
# Name associated with the maximum value
MaxName = df['Names'][df['Births'] == df['Births'].max()].values
MaxName
# Text to display on graph
Text = str(MaxValue) + " - " + MaxName
Text
# Add text to graph
plt.annotate(Text, xy=(1, MaxValue), xytext=(8, 0), 
                 xycoords=('axes fraction', 'data'), textcoords='offset points')


print("The most popular name")
df[df['Births'] == df['Births'].max()]
#Sorted.head(1) can also be used



print(np.random.seed(500))
np.random.seed(10)
random_names = [names[random.randint(low=0,high=len(names))] for i in range(1000)]

# Print first 10 records
random_names[:10]

# The number of births per name for the year 1880
births = [random.randint(low=0,high=1000) for i in range(1000)]
births[:10]

#Merge the names and the births data set using the zip function.
BabyDataSet = list(zip(random_names,births))
BabyDataSet[:10]

df = pd.DataFrame(data = BabyDataSet, columns=['Names', 'Births'])
df[:10]
df

df.to_csv('births1880.txt',index=False,header=False)

#Get Data
Location = r'births1880.txt'
df3 = pd.read_csv(Location)

df3.info()

df.head()
df = pd.read_csv(Location, header=None)
df.info()
df.shape
df.tail()

df = pd.read_csv(Location, names=['Names','Births'])
df.head(5)

#Prepare Data
# Method 1:
df['Names'].unique()

# If you actually want to print the unique values:
for x in df[0].unique():
    print(x)
    
# Method 2:
print(df['Names'].describe())

# Create a groupby object
name = df.groupby('Names')
name

# Apply the sum function to the groupby object
df4 = name.sum()
df

#Analyze Data
# Method 1:
Sorted = df.sort_values(['Births'], ascending=False)
Sorted.head(1)

# Method 2:
df['Births'].max()

#Present Data # Create graph

df['Births'].plot.bar()

print("The most popular name")
df.sort_values(by='Births', ascending=False)

