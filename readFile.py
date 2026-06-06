# Create a program that opens file.txt. Read each line of the file and prepend it with a line number.

with open('readFile.txt') as file:
  line_number = 1
  for line in file:
    print('{}: {}'.format(line_number, line.rstrip()))
    line_number += 1