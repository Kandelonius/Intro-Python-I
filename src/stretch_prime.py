import sys
import math

num = int(sys.argv[1])
compare = 2
compare_boolean = True
count = 0
# print(num)

while(compare < (num / 2)):
    if(num % compare == 0):
        count += 1
        compare_boolean = False
        break
    else:
        count += 1
        compare += 1


if(compare_boolean):
    print(f"using half method {num} is prime, took {count} iterations")
else:
    print(f"using half method {num} is not prime, took {count} iterations")
    print(f"It is divisible by {compare}")
print(f"{count} before")
compare = 2
compare_boolean = True
count = 0
print(f"{count} after")
while(compare < math.sqrt(num)):
    if(num % compare == 0):
        count += 1
        compare_boolean = False
        break
    else:
        count += 1
        compare += 1

if(compare_boolean):
    print(f"using square root method {num} is prime, took {count} iterations")
else:
    print(f"using square root method {num} is not prime, took {count} iterations")
    print(f"It is divisible by {compare}")