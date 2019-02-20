# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 16:08:58 2018

@author: IOA
"""

import random

greetings = ['hola', 'hello', 'hi', 'Hi', 'hey!','hey']
random_greeting = random.choice(greetings)

question = ['How are you?','How are you doing?']
responses = ['Okay',"I'm fine"]
random_response = random.choice(responses)

userInput = 1
while userInput != 'q':
	userInput = input(">>> (type q to quit) :    ")
	if userInput in greetings:
		print(random_greeting)
	elif userInput in question:
		print(random_response)
	else:
		print("I did not understand what you said")