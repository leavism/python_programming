# 13.2 Text Input and Output
'''
An absolute filename contains a filename with its complete path and drive letter, c:\pybook\scores.txt
A relative filename is relative to its current working directory.
Files can be classified into text or binary files. A file that can be processed (that is, read, created, or modified) using a text editor is called
a text file. All other files are called binary files.
'''

# 13.2.1 Opening a File
'''
You need to first creat e file object that is associated with a physical file. The syntax for opening a file is:

filevariable = open(filename, mode)

The open function returns a file object for filename. The mode parameter is a string that specifies how the files will be used (for reading or writing).

"r" - opens a file for reading
"w" - opens a new file for writing. If the file already exists, its old contents are destroyed
"a" - opens a file for appending data from the end of the file
"rb" - opens a file for reading binary data
"wb" - open a files for writing binary data

The following statement opens a file named scores.txt in the current directory for reading:
'''

# input = open("scores.txt", "r")

            # You can also use the absolute filename to open the file in Windows

# input = open(r"c:\pybook\scores.txt", "r")

'''
The statement opens the file scores.txt that is in the c:\pybook directory for reading. The r prefix before the absolute filename specifies that the string
is a raw string, which causes python interpreter to treat backlash characters as literal backslashes.
'''

# 13.2.2 Writing Data
'''
The open function creates a file object, which is an instance of the _io.TextIOWrapper class. This class contains the methods for reading and writing data
for closing the files:

read([number.int]): str - returns the specified number of characters from the file. If argument is omitted, entire remaining contents in file are read
readline(): str         - returns the next line of the file as a string
readlines(): list       - returns a list of the remaining lines in the file
write(s: str): None     - writes the string to the file
close(): None           - closes the file
'''

def main():
    # Open file for output
    outfile = open("President.txt", "w")
    
    # Write data to file
    outfile.write("Bill clinton\n")
    outfile.write("George Bush\n")
    outfile.write("Barack Obama")

    outfile.close() # Close the output file

main()

'''
This programs creates/opens a file named Presidents.txt using the w mode for writing data. The program invokes the write method on the file object to write
three strings
'''

# 12.2.3 Testing a file's existence
'''
To prevent data in an existing file from being erased by accident, you should test to see if the file exists befpre p[emomg ot fpr writhing. The isfile function
in the os.path module can be used to determine whether a file exists.
'''
'''
import os.path
if os.path.isfile("President.txt"):
    print("President.txt exists")
else:
    print("No")
'''
# 13.2.4 Reading Data
'''
After a file opened for reading data, you can use the read method to read a specified number of characters or all characters from the file and return
them as a string, the readline() method to read the next line, and the readlines() method to read all the lines into a list of strings.
'''

# 13.2.5 Reading All Data from a File
'''
Programs often need to read all data from a file. Here are two common approaches to accomplishing this task:

1. use the read() method to read all data from the file and return it as one string
2. Use the readlines() method to read all the data and return it as a list of strings

These are good for reading small files. If the file is too big to be stored in the memory, write a loop to read one line at a time, process it, and continue
reading the next line until it reaches the end.
'''
'''
line = infile.readline() # REad a line
while line != "":
    #Process the line here
    #Read next line
    line = infile.readline()

'''
'''
Python also lets you read all lines by using a for loop:
'''

# 13.2.7 Writing and Reading Numeric Data
'''
To write numbers to a file, you must convert them into strings and then use the write method to the file. In order to read the numbers back correctly,
separate them with whitespace characters such as " " or \n.
'''

from random import randint

def main1():
    # Open file for writing data
    outfile = open("Numbers.txt", "w")
    for i in range(10):
        outfile.write(str(randint(0, 9)) + " ")
    outfile.close() # Close the file
        
    # Open file for reading data
    infile = open("Numbers.txt", "r")
    s = infile.read()
    numbers = [eval(x) for x in s.split()]
    for number in numbers:
        print(number, end = " ")
    infile.close()
    
main1()
