#!/usr/bin/env python3

''' 
Create a function that prompts the user for a name
then takes the name and greets it with another function
'''

# Function to get name
def get_name():
  name = input("What is your name? ")
  return name

# Function to greet user
def say_hi(name): 
  print('Hi {}!'.format(name))

# Function that calls both functions
def greet_name():
  '''Get and display name'''
  name = get_name()
  say_hi(name)

greet_name()

## This print the comment associated with function to help user identify what the function does
#help(say_hi) 
