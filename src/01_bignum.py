import math

# Print out 2 to the 65536 power
# (try doing the same thing in the JS console and see what it outputs)

# print(math.pow(2, 65536)) # OverflowError: math range error
print(f"2^50 is {math.pow(2, 50)}")
print(f"Some unreasonably long number is {2 ** 65536}")
