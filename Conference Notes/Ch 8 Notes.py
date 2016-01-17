# 8.2.1 The str class

''' 
You can create strings using the constructor:
'''
s1 = str()
s2 = str("Welcome")

''' or '''

s1 = ""
s2 = "Welcome"

''' String object is immutable'''

# 8.2.2 Functions for strings

''' You can use the len function to return the number of characters in a string, and the max and min functions to return the largest or smallesst
character in a string'''

s = "Welcome"
print(len(s))
print(max(s))
print(min(s))

# 8.2.3 Index Operator []
'''
A string is a sequence of characters. A character in a string can be accessed through the index operator using the syntax:

s[index]
'''

s = "Welcome"
for i in range(0, len(s), 2):
	print(s[i], end = "")

# 8.2.4 The Slicing Operator [start : end]
s = "Welcome"
print()
print(s[1:4])
print(s[4:])
