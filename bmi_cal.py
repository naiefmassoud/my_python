#!/usr/bin/env python3

# Calculate the BMI of the User based on their input

height = float(input("Enter your height in meters: "))

weight = float(input("Enter your weight in kgs: "))

bmi = weight / height ** 2

# Round the float number to 2 decimal places, instead of having 3.333333 you get 3.33
bmi = round(bmi, 2)

if bmi < 18.5:
    weight_class = "You are underweight. A healthy weight is between 18.5 and 24.9"
elif bmi >= 18.5 and bmi <= 24.9:
    weight_class = "You are within the Healthy Weight range"
else:
    weight_class = "You are overweight. A healthy weight is between 18.5 and 24.9"

#print("Your BMI Index is: " + str(bmi) )
print(f"Your BMI Index is: {bmi}")
print(weight_class)