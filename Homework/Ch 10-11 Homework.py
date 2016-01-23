# 10.1

gradeLetters = ["A", "B", "C", "D", "F"]
s = input("Enter scores: ")
scores = s.split()
entered = [eval(x) for x in scores]

def gradeCalc(input):
    if input >= max(entered) - 10:
        return "A"
    elif input >= max(entered) - 20:
        return "B"
    elif input >= max(entered) - 30:
        return "C"
    elif input >= max(entered) - 40:
        return "D"
    else:
        return "F"

for i in range(0, len(entered)):
    print("Student",i,"score is",entered[i],"and grade is", gradeCalc(entered[i]))
''' Results:
Enter scores: 40 55 70 58
Student 0 score is 40 and grade is C
Student 1 score is 55 and grade is B
Student 2 score is 70 and grade is A
Student 3 score is 58 and grade is B


Enter scores: 100 90 80 70 65 55 75 92 50 32
Student 0 score is 100 and grade is A
Student 1 score is 90 and grade is A
Student 2 score is 80 and grade is B
Student 3 score is 70 and grade is C
Student 4 score is 65 and grade is D
Student 5 score is 55 and grade is F
Student 6 score is 75 and grade is C
Student 7 score is 92 and grade is A
Student 8 score is 50 and grade is F
Student 9 score is 32 and grade is F
'''

# 10.13

s = input("Enter ten numbers: ")
splitting = s.split()
entered = [eval(x) for x in splitting]

def eliminateDuplicates(lst):
    temp = []
    for x in lst:
        if x not in temp:
            temp.append(x)
    print(temp)

eliminateDuplicates(entered)

''' Results:
Enter ten numbers: 1 2 3 2 1 6 3 4 5 2
[1, 2, 3, 6, 4, 5]
'''
# 10.16

def shortBubbleSort(lst):
    swap = True
    values = len(lst) - 1
    while values > 0 and swap:
       swap = False
       for i in range(values):
           if lst[i]>lst[i+1]:
               swap = True
               temp = lst[i]
               lst[i] = lst[i+1]
               lst[i+1] = temp
       values = values-1

entered = [45, 23, 65, 40, 20, 46, 76, 93, 50, 39]
shortBubbleSort(entered)
print(entered)

'''
 Results
[20, 23, 39, 40, 45, 46, 50, 65, 76, 93]
'''

# 11.1
def sumColumn(m, columnIndex):
    matrix = []
    for row in range(m):
        matrix.append(input("Enter a 3-by-4 matrix row for row: ").split())

    T2 = [[float(column) for column in row] for row in matrix]

    for column in range(len(T2[columnIndex])):
        total = 0
        for row in range(len(T2)):
            total += T2[row][column]
        print("Sum for column",column,"is",total)

sumColumn(3, 0)

''' Results:
Enter a 3-by-4 matrix row for row:1.5 2 3 4
Enter a 3-by-4 matrix row for row:5.5 6 7 8
Enter a 3-by-4 matrix row for row:9.5 1 3 1
Sum for column 0 is 16.5
Sum for column 1 is 9.0
Sum for column 2 is 13.0
Sum for column 3 is 13.0

Enter a 3-by-4 matrix row for row: 1 2 3 4
Enter a 3-by-4 matrix row for row: 5 6 7 8
Enter a 3-by-4 matrix row for row: 9 10 11 12
Sum for column 0 is 15.0
Sum for column 1 is 18.0
Sum for column 2 is 21.0
Sum for column 3 is 24.0
'''
