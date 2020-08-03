# Write a function is_even that will return true if the passed-in number is even.

def is_even(a):
    return (a % 2 == 0)

odd_or_even = input("Enter a number to be evaluated ")
print(is_even(int(odd_or_even)))

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

if(num % 2 == 0):
    print("even")
else:
    print("odd")
