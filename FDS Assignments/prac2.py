def accept_data(A):
    n = int(input("Enter number of students: "))
    for i in range(n):
        marks = int(input("Enter the Marks of student %d : (Enter -1 if Absent)"%(i+1)))
        A.append(marks)

def show_data(A):
    n = len(A)
    print("Student's Marks list is as follows :")
    for i in range(n):
        if (A[i] != -1):
            print("Marks of student %d :"%(i+1),A[i])
        else:
            print("Marks of student %d :"%(i+1),"Absent")

def average(A):
    summ = 0
    count = 0
    for mark in A:
        if mark != -1:
            summ += mark
            count += 1
    print(count,summ)
    if count!=0:
        avg = summ/count
        return avg
    else:
        return 0


def maxscore(A):
    max_score = 0
    for i in range(len(A)):
        if A[i] > max_score:
            max_score = A[i]
    return max_score

def minscore(A):
    min_score = A[0]
    for i in range(len(A)):
        if A[i] < min_score and A[i] != -1:
            min_score = A[i]
    return min_score

def absent(A):
    count = 0
    for i in range(len(A)):
        if A[i] == -1:
            count  += 1
    return count

def freq(A):
    highfreq = 0
    freq = 0
    for i in range(len(A)):
        for j in range(len(A)):
            if  A[i] == A[j]:
                freq += 1

        if freq > highfreq:
            highfreq = freq
            hmarks = A[i]
        freq = 0   

    return (highfreq,hmarks)

def main():
    students = []
    while True:

        print("1 - Accept Information")
        print("2 - The Average Score of the Class ")
        print("3 - Highest Score and Lowest Score of the Class ")
        print("4 - Count of Students who were Absent for the Test ")
        print("5 - Display Marks with Highest Frequency ")
        print("6 - Exit")

        ch = int(input("Enter your Choice number: "))

        if (ch == 1):
            accept_data(students)
            show_data(students)
        
        elif (ch == 2):
            ans = average(students)
            print("The Average Score of the Class is: ", ans)


        elif (ch == 3):
            maxmarks = maxscore(students)
            minmarks = minscore(students)
            print("The Highest Score is: ",maxmarks)
            print("The Lowest Score is: ",minmarks)


        elif (ch == 4):
            count = absent(students)
            print("The Number of Students Absent for the Test is : ",count)

        elif (ch == 5):
            (hfreq_marks,hmarks) = freq(students)
            print("The Marks with Highest Frequency of ",hfreq_marks,"are: ",hmarks)

        elif (ch == 6):
            print("End of Program!!")
            break

        else:
            print("Invalid Option!!")

main()
