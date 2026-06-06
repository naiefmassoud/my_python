#!/usr/bin/env python3

# Test the compatibility between two people

# Take both their names and then check the number of times the letters from TRUE occur
name_1 = input("Enter girl's name: ")
name_2 = input("Enter guy's name: ")
couple_names = name_1 + name_2
couple_names = couple_names.lower()
#print(couple_names)

t = couple_names.count("t")
r = couple_names.count("r")
u = couple_names.count("u")
e = couple_names.count("e")
true_count = t + r + u + e
#print(str(true_count))

# Check the number of times the letters from LOVE occur
l = couple_names.count("l")
o = couple_names.count("o")
v = couple_names.count("v")
e = couple_names.count("e")
love_count = l + o + v + e
#print(str(love_count))

score = str(true_count) + str(love_count)
#print(score)
score = int(score)

print("The Love Calculator is calculating your score...")

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you go together like chocolate and peanut butter")
else:
    print(f"Your score is {score}")