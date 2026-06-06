#!/usr/bin/env python3

## Ask user how far they want to travel, then suggest transportation method

# Prompt user for distance
distance = int(input('How many km do you want to travel: '))

# Conditionals
if distance <= 3:
  print('I suggest walking to your destination')
elif distance > 3 and distance < 300:
  print('I suggest driving to your destination')
else:
  print('I suggest flying to your destination')
