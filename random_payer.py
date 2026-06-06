# Select a random name from a list. The person selected will pay the bill
import random

names_string = input("Provide a list of comma seperated names to choose from: ")

# Split the string into a list of names with delimeter comma then space
names = names_string.split(", ")

# Get the total number of items in the list
num_items = len(names)

# Generate random number between 0 and last index
random_choice = random.randint(0, num_items - 1)

print(names[random_choice] + " should pay the bill")
    