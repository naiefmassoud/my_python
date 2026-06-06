#!/usr/bin/env python3
## Count number of letters in a name given by user
# Prompt user for name
name = input("Enter Name to Count Its Letters:")

# Count letters in name
name_len = len(name)

# Print results
print(name + " is " + str(name_len) + " characters long")