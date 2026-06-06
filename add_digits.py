# The function takes a two digit number from the user and adds each digit to the other

two_digit_number = input("Type a two digit number: ")

#print(type(two_digit_number))

add_the_digits = int(two_digit_number[0]) + int(two_digit_number[1])

print("The sum of your two digits is: " + str(add_the_digits))
