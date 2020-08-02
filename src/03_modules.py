"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# print(f"the command line arguments are {sys.argv}")
# argument_length = len(sys.argv)
print(f"full sys.argv is {sys.argv[0]}")
print("command line argument path is:")
print(sys.argv[0].replace('\\', '\n'))

# Print out the OS platform you're using:
print(f"os platform is: {sys.platform}")

# Print out the version of Python you're using:
print(f"python version is: {sys.version_info[0]}.{sys.version_info[1]}")


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print(f"current process id is: {os.getpid()}")

# Print the current working directory (cwd):
print(f"current working directory is: {os.getcwd()}")

# Print out your machine's login name
print(f"login name is: {os.getlogin()}")
