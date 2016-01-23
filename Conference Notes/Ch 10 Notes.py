# 10.1 Introduction
'''
Programs often need to store a large number of values. An efficient way to organize the data
is with a type called a list that stores a sequential collection of elements.
'''

number_of_elements = 5 # how many times to ask for input (how many number of values to store)
numbers = [] # Stores all the numbers here
sum = 0

for i in range(number_of_elements):
    value = eval(input("Enter a new number: "))
    numbers.append(value) # Appends the numbers inputted into the list numbers
    sum += value # Adds the inputted numbers together

average = sum / number_of_elements # Calculates the average

count = 0
for i in range(number_of_elements):
    if numbers[i] > average:
        count += 1

print("The average is", average)
print("Number of elements above the average is", count)

# 10.2 List Basics

'''
The list class defines lists.
'''

list1 = list() # Creates an empty list
list2 - list([2, 3, 4]) # Creates a list with elements 2, 3, 4
list3= list(["red", "green", "blue"]) # Creates a list with strings
list4 = list(range(3, 6)) # Creates a list with elements 3, 4, 5
list5 = list("abcd") # Creates a list with characters a, b, c, d

list1 = [] # Alternative way to write list1
list2 - [2, 3, 4] # Alternative way to write list2
list3 = ["red", "greeb"] # Alternative way to write list3

# 10.2.2 List of a Sequence Type

x in s # True if element x is in sequence s
x not in s # True if element x is not in sequence s
s1 + s2 # Concatenates two sequences in s1 and s2
s * n, n * s # n copies of sequence s
s[i] # ith element in sequence s
s[i : j] # Slice of sequences from index i to (j - 1)
len(s) # Length of sequence s
min(s) # The smallest element of sequence s
max(s) # The largest element of sequence s
sum(s) # Sum of all numbers in sequence s
for loop # Traverse elements from left to right in a for loop
<, <= , >, >=, =, != # Compares two sequences

# 10.2.3 Functions for Lists

>>>List1 = [2,3,4,5,1,32]
>>>len(list1)
5
>>>max(list1)
32
>>>min(list1)
1
>>>import random
>>>random.shuffle(list1) # Randomly shuffles the elements in list1
>>>list1
[4,1,2,32,3]
>>>

# 10.2.4 Index Operator []
'''
An element in a list can be accessed through the index operator, using the following:
myList[index]
'''

>>>myList = [5,6,4.5,3.3,13.2,4.0,34.33,34.0,45.45,99.993,11123]
>>>myList[0]
5
>>>myList[1]
6
>>>myList[9]
11123
>>>myList[5]
34.33

'''
myList[index] can be used like a variable, so it is known as an index variable. For example:
'''

myList[2] = mylist[0] + myList[1] # Adds the values of myList[0] and myList[1] to mylist[2]

'''
The following loop assigns 0 to myList[0], 1 to myList[1], ..., and 9 to myList[9]
'''

for i in range(len(myList)):
    myList[i] = i

# 10.2.5 List Slicing [start : end]
'''
The slicing operator returns a slice of the list using the syntax list[start : end]. The slice is a sublist from index start to index end - 1
'''
>>>list1 = [2, 3, 5, 7, 9, 1]
>>>list1[2:4]
[5,7]
>>>list1[:2]
[2,3]

# 10.2.7 TraversingElements in a for loop
'''
The elements in a Python list are iterable. Python supports a for loop, which enables  you to traverse the list sequuentially without
using the index variable.
'''

for u in myList:
    print(u)

'''
You still have to use an index variable if you wish to traverse the list in a different order or change the elements in the list. For
example, the following code displays the elements at an odd-numbered positions.
'''

for i in range(0, len(myList), 2):
    print(myList[i])

# 10.2.9 List Comprehensions
'''
List comprehensions provide a concise way to create a sequential list of elements. A list comprehension consists of brackets containing an expression
followed by a for clause, then zero or more for or if clauses. The list comprehension produces a list with the results from eevaluating the expression
'''

>>>list1 = [x for x in range(5)] # Returns a list of 0, 1, 2, 3, 4
>>>list1
[0, 1 , 2, 3, 4]
>>>
>>>list2 = [0.5 * x for x in list 1]
>>>list2
[0.0, 0.5, 1.0,1.5, 2.0]
>>>
>>>list3 = [x for x in list2 if x < 1.5]
>>>list3
[0.0., 0.5, 1.0]
>>>

# 10.2.10 List Methods

append(x : object): none # Adds an element x to the end of the list
count(x : object): int # Returns the number of times element x appears in the list
extend(l : list): none # Appends all the elements in l to the list
index(x : object): int # REturns the index of th efirst occurance of element x in the list
insert(index : int, x: object): none # Insterts an element x at a given index. Note that the first element in the list has index 0
pop(i): object # Removes the element in the given position and returns it. The paramter i is optional. If it is not specified, list.pop() removes and returns the last element on the list
remove(x: object): none # Removes the first occurence of element x from the list
reverse(): none # reverse the elements in the list
sort(): none # Sorts the elements in the list in ascending order

>>>list1 = [2, 3, 4, 1, 32, 4]
>>>list1.append(19)
>>>list1
[2, 3, 4, 1, 32, 4, 19]
>>>list1.count(4) # returns the count for number 4
2
>>>list2 = [99, 54]
>>>list1.extend(list2)
>>>list1
[2, 3, 4, 1, 32, 4, 19, 99, 54]
>>>list1.index(4) # Return the index of number 4
2
>>>list1.insert(1, 25) # Inserts 25 at position index 1
>>>list1
[2, 25, 3, 4, 1, 32, 4, 19, 99, 54]
>>>

>>>list1 = [2, 25, 3, 4, 1, 32, 4, 19, 99, 54]
>>>list1.pop(2)
3
>>>list1
[2, 25, 4, 1, 32, 4, 19, 99, 54]
>>>

# 10.2.11 Splititng a String into a List
'''
The str class contains the split method, which is useful for splitting items in a string into a list.
'''

items = "Jane John Peter Suan".split()

'''
splits the string Jane John Peter Susan into the list ["Jane", "John", "Peter", "Susan"]
'''

items = "09/20/2012".split("/")

'''
splits the string into the list ["09", "20", "2012"]
'''

# 10.2.12 Inputting Lists
'''
You may often need code that reads data from the console into a list. You can enter one data item per line and append it to a list in a loop:
'''

lst = [] # creates a list
print("Enter 10 numbers: ")
for i in range(10)
    lst.append(eval(input))

'''
Sometimes it's more convenient to enter the data in one line separated by spaces:
'''

s = input("Enter 10 unmbers separated by spaced from one line: ")
items = s.split() # extract items from the list
lst = [eval(x) for x in items] # converts items into numbers

# 10.2.13
'''
Sometimes you need to shift elemetns left or right. Python does not provide such a methon in the lsit class.
'''

def shift(lst):
    temp = lst[0] # retrain the first element

    #shift elements left
    for i in range(1, len(lst)):
        lst[i-1] = lst[i]
    #move the first element to fill in the last position
    lst[len(lst) - 1] = temp

# 10.7 Passing Lists to Functions
'''
Since list is an object, passing a list to a funtion is like passing an object to a function
'''

def printList(lst):
    for element in lst:
        print(element)

printList([3, 1, 2, 6, 4, 2])
list1 = [1, 2, 3, 4, 5]
printList(list1)

# 10.8 Returning a List from a function
'''
You can pass list arguments when invoking a function. A function can also return a list.
'''

def reverse(lst):
    result = [] # Creates new list

    for element in list: # Copy elements from list name lst to the list named result
        result.insert(0, element)

    return result

# 10.10 Searching Lists
'''
Searching is a common task in computer programming. This section discusses two commonly used approaches: linear searches and binary searched.
'''

# 10.10.1 The Linear Search Approach
'''
THe linear search approach compares the key element key sequentially with each element ini the list. It continues to do so until the key matches an
element in the list or the list is exhuasted without a match being found. If ia match is found, the linear search returns the matching element's index in the list.
If no match is found, the search returns -1.
'''

def linearSearch(lst, key):
    for i in range(len(lst)):
        if key == lst[i]:
            return i
    return -1

# 10.10.2 The binary Search Approach
'''
The binary search is the other common search approach for a list of values. For a binary search to work, the leements in the list must already be ordered.
Assume that the list is in ascending order. A binary search first compares the key with the  element in the middle of the list.
    - If the key is less than the list's middle element, you need to continue the search for the key in only the first half of the list
    - If the key is equal to the list's middle element, the search ends with a mathch
    - IF the key is greater than the list's middle element, you need to continue to search for the key in only the second ohalf of the list
'''

def binarySearch(lst, key):
    low = 0
    high = len(lst) - 1

    while high >= low:
        mid = (low + high) // 2
        if key < list[mid]:
            high = mid - 1
        elif key == list[mid]:
            return mid
        else:
            low = mid + 1
    return -low - 1

# 10.11.1 Selection Sort
'''
Suppose you want to sort a list in ascending order. A selection sort finds the smallest element in the list and swaps it with the first element.
It then finds the smallest element remaining and swaps it with the first element in the remaining list, and so on.
'''

def selectionSort(lst):
    for i in range(len(lst) - 1):
        # Find the minimum in the lst[i : len(lst)]
        currentMin = lst[i]
        currentMinIndex = i

        for j in range(i + 1, len(lst)):
            if currentMin > lst[j]:
                currentMin = lst[j]
                currentMinIndex = j

        #Swap lst[i] with lst[currentMinIndex] if necessary
        if currentMinIndex != i:
            list[currentMinIndex = lst[i]
                 lst[i] = currentMin

# 10.11.2 Insertion Sort
'''
Suppose that you want to sort a list in ascending order. The insertion sort algorithm sorts a list of values by repeatedly inserting a new element
into a sorted sublist unitl the whole list is sorted.
'''

def insertionSort(lst):
    for i in range(1, len(lst)):
        # insert lst[i] into a sorted sublist lst[ 0 : i] so that lst[0 : i + 1] is sorted
        currentElement = lst[i]
                 k = i - 1
                 while k >= 0and lst[k] > current Element:
                 lst[k + 1] = lst[k]
                 k -= 1

                 # instert the current element into lst[k + 1]
                 lst[k + 1] = currentElement
