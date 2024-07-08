def accept_data(A):
    n = int(input("Enter number of students: "))
    for i in range(n):
        marks = int(input("Enter the Marks of student %d: (Enter -1 if Absent) " % (i + 1)))
        A.append(marks)

def show_data(A):
    if not A:
        print("Student's Marks list is empty.")
        return
    print("Student's Marks list is as follows: ", end="")
    for i in range(len(A) - 1):
        print(A[i], end=", ")
    print(A[-1])

def average(A):
    sum = 0
    count = 0
    for marks in A:
        if marks != -1:
            sum += marks
            count += 1
    return sum / count if count != 0 else 0

def max_score(A):
    max_score = -1
    for marks in A:
        if marks > max_score:
            max_score = marks
    return max_score

def min_score(A):
    min_score = float('inf')
    for marks in A:
        if marks != -1 and marks < min_score:
            min_score = marks
    return min_score if min_score != float('inf') else None

def absent(A):
    return A.count(-1)

def freq(A):
    frequency = {}
    for marks in A:
        if marks != -1:
            frequency[marks] = frequency.get(marks, 0) + 1

    high_freq = max(frequency.values(), default=0)
    high_freq_marks = [marks for marks, freq in frequency.items() if freq == high_freq]

    return high_freq_marks

def main():
    students = []

    while True:
        print("1 - Accept Information")
        print("2 - The Average Score of the Class")
        print("3 - Highest Score and Lowest Score of the Class")
        print("4 - Count of Students who were Absent for the Test")
        print("5 - Display Marks with Highest Frequency")
        print("6 - Exit")

        ch = int(input("Enter your Choice number: "))

        if ch == 1:
            accept_data(students)
            show_data(students)

        elif ch == 2:
            ans = average(students)
            print("The Average Score of the Class is: ", ans)

        elif ch == 3:
            maxmarks = max_score(students)
            minmarks = min_score(students)
            if minmarks is None:
                print("No scores to display.")
            else:
                print("The Highest Score is: ", maxmarks)
                print("The Lowest Score is: ", minmarks)

        elif ch == 4:
            count = absent(students)
            print("The Number of Students Absent for the Test is: ", count)

        elif ch == 5:
            hfreq_marks = freq(students)
            print("The Marks with Highest Frequency are: ", hfreq_marks)

        elif ch == 6:
            print("End of Program!!")
            break

        else:
            print("Invalid Option!!")

main()
