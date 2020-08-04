"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

import sys
# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

print(f"full sys.argv is {sys.argv}")
f = open('c:\\Users\\Shane\\Desktop\\Class-Folder\\Intro-Python-I\\src\\foo.txt')
print(f.read())
f.close()


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

b = open('c:\\Users\\Shane\\Desktop\\Class-Folder\\Intro-Python-I\\src\\bar.txt', 'w')
b.write('\nWho will believe my verse in time to come,\nIf it were filled with your most high deserts?\nThough yet heaven knows it is but as a tomb\nWhich hides your life, and shows not half your parts.\nIf I could write the beauty of your eyes,\nAnd in fresh numbers number all your graces,\nThe age to come would say \'This poet lies;\nSuch heavenly touches ne\'er touched earthly faces.\'\nSo should my papers, yellowed with their age,\nBe scorned, like old men of less truth than tongue,\nAnd your true rights be termed a poet\'s rage\nAnd stretched metre of an antique song:\nBut were some child of yours alive that time,\nYou should live twice, in it, and in my rhyme.')
b.close()
b = open('c:\\Users\\Shane\\Desktop\\Class-Folder\\Intro-Python-I\\src\\bar.txt')
print(b.read())
b.close()