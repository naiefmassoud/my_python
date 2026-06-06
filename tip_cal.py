#!/usr/bin/env python3

# Calculate the tip based on bill, number of people, and tip percentage

print("Welcome to the tip calculator!")

bill = float(input("What is the total bill: $"))

tip_percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))

num_of_ppl = int(input("How many people are splitting the bill? "))

each_before_tip = bill / num_of_ppl

tip = each_before_tip * tip_percentage / 100 

total_each = each_before_tip + tip

total_each_rounded = round(total_each, 2)

print(f"Each person should pay: ${total_each_rounded}")