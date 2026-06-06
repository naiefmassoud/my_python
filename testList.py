#!/usr/bin/env python3

## List of animals and prompt user for more animals to add to the list

# Create List of Animals
animals = ['cat', 'dog', 'lizard']

# Function to print list of animals
def animal_pl():
  for animal in animals:
    print(animal)

# Show current list
print("The current list of animals:")
animal_pl()

# Add animal from user input
new_animal = ''
while new_animal != 'stop':
  new_animal = input("Add animal: ")
  animals.append(new_animal)
else:
 print("------List updated------")

# Show new list of animals
print("The new list of animals:")
animal_pl()

