#!/usr/bin/env python3

"""
Print a picture of a cat and,
make it say whatever the user inputs
"""

## Set variables
# Get input from the user
text = input("What would you like the cat to say? ")

# Determine the length of the input
text_length = len(text)

# Make the border the same size as the input
print('              {}'.format('_' * text_length))
print('           <  {}  >'.format(text))
print('              {}'.format('-' * text_length))
# Show the cat
print('             /')
print('   /\_/\   /')
print(' (  o.o  ) ')
print('  >  ^  < ')

