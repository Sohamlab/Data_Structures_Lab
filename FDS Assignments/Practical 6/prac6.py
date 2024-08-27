# Practical 6 Quick sort

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

def partition(p, low, high):
    pivot = low
    left = low + 1
    right = high

    while right >= left:
        while left <= high and p[left] <= p[pivot]:
            left += 1
        while p[right] > p[pivot]:
            right -= 1

        if left < right:
            p[left], p[right] = p[right], p[left]

    p[pivot], p[right] = p[right], p[pivot]
    return right


def quick_sort(p, low, high):
    if low < high:
        part = partition(p, low, high)
        quick_sort(p, low, part - 1)
        quick_sort(p, part + 1, high)



def main():
    p = []
    A = []

    while True:
        print("1 - Enter Student Percentages")
        print("2 - Display Roll-no wise List")
        print("3 - Sort using Quick Sort")
        print("4 - Exit program")

        choice = int(input("Enter the no of Operation to be Performed: "))

        if choice == 1:
            accept(A, p)
            print("Marks Entered Succesfully!")

        elif choice == 2:
            show_all(A)

        elif choice == 3:
            quick_sort(p,0,len(p)-1)
            print("The Sorted List is: ")
            print(p)
            show_top(p)

        elif choice == 4:
            break

        else:
            print("Invalid Choice!!")

main()
