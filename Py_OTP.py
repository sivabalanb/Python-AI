# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 11:30:50 2019

@author: IOA
"""
#Generate 4 digit Numeric OTP

# import library 
import math, random 
  
# function to generate OTP 
def generateOTP() : 
  
    # Declare a digits variable   
    # which stores all digits  
    digits = "0123456789"
    OTP = "" 
  
   # length of password can be chaged 
   # by changing value in range 
   #This python math.floor function is used to return the closest integer 
   #value which is less than or equal to the specified expression or Value
    for i in range(4) : 
        OTP += digits[math.floor(random.random() * 10)] 
  
    return OTP 
  
# Driver code 
if __name__ == "__main__" : 
      
    print("OTP of 4 digits:", generateOTP()) 