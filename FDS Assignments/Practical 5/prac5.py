# Practical 5 Selcetion sort, Bubble sort

def accept(A,p):
    n = int(input("Enter the number of Students"))
    print("Give the Percentage of Students Roll-no wise: ")
    for i in range(n):
        details = []
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))
        details.append(name)
        details.append(marks)
        A.append(details)
        p.append(marks)

def show_all(A):
    n = len(A)
    print("The Percentage Obtained (Roll-no wise) are: ")
    print("Name","\t","| Percentage")
    print("--------------------------------")
    for i in range(n):
        print(A[i][0],"\t\t",A[i][1])

def show_top(p):
    print("The Top-Five scores are: ")
    for i in range(1,6):    
        print(i,p[-i])


def selection_sort(p):
    n = len(p)
    for i in range(n):
        minind = i
        for j in range(i+1,n):
            if (p[j] < p[i]):
                minind = j
        
        if (i != minind):
            temp = p[i]
            p[i] = p[minind]
            p[minind] = temp

    return p

def bubble_sort(p):
    n = len(p)
    for i in range(n):
        for j in range(n-i-1):
            if (p[j] > p[j+1]):
                temp = p[j]
                p[j] = p[j+1]
                p[j+1] = temp


def main():
    p = []
    A = []

    while True:
        print("1 - Enter Student Percentages")
        print("2 - Display Roll-no wise List")
        print("3 - Sort using Selection Sort")
        print("4 - Sort using Bubble sort")
        print("5 - Exit program")

        choice = int(input("Enter the no of Operation to be Performed: "))

        if choice == 1:
            accept(A, p)
            print("Marks Entered Succesfully!")

        elif choice == 2:
            show_all(A)

        elif choice == 3:
            selection_sort(p)
            show_top(p)

        elif choice == 4:
            bubble_sort(p)
            show_top(p)

        elif choice == 5:
            break

        else:
            print("Invalid Choice!!")

main()