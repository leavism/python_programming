# 11.2 Processing Two-Dimensional Lists
'''
You can think of two-dimensional list as a list that consists of rows.
'''

matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 0, 0, 0],
    [0, 1, 0 ,0 ,0],
    [0 ,0 ,9 ,0 ,3],
    ]

# 11.2.1 Initializing Lists with Input Values
'''
The following loop initializes the matrix with user input values:
'''

matrix = []

numberOfRows = eval(input("Enter the number of rows: "))
numberOfColumns = eval(input("Enter number of columns: "))
for row in range(numberOfRows):
    matrix.append([])
    for column in range(numberOfColumns):
        value = eval(input("Enter an element and press enter: "))
        matrix[row].append(value)

print(matrix)

# 11.2.3 Printing Lists
'''
To print a two-dimensional list, you have to print each element in the list by using a loop like the following:
'''

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    ]

for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        print(matrix[row][column], end=" ")
    print()

# 11.2.4 Summing All Elements
'''
Using a variable named total to store the sum. Initally, total is 0. Add each element in the list to total by using a loop like this:
'''

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    ]

total = 0
for row in matrix:
    for value in row:
        total += value
print("Total is", total)

# Summing Elements by Column
'''
For each column, use a variable named total to store its sum. Add each element in the colun to total using a loop like:
'''
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    ]

for column in range(len(matrix[0])):
    total = 0
    for row in range(len(matrix)):
        total += matrix[row][column]
    print("Sum for column",column,"is",total)

# 11.3 PAssing Two-Dimensional Lists to Functions
'''
You can pass a two-dimensional list to a function just as you pass a one-dimensional list. The function getMatrix() returns a two-dimensional list. The
function accumulate(m) returns the sum of all elements in a matrix
'''



