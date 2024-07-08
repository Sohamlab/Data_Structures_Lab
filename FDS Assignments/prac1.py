def accept_data(A, str):
    n = int(input("Enter number of students who play %s : "%str))
    for i in range(n):
        name = input("Enter the name of student %d : "%(i+1))
        A.append(name)

def show_data(A, str):
    n = len(A)
    print("Students who play %s :"%str, end = "")
    for i in range(n-1):
        print(A[i], end=",")
    print("%s"%A[n-1])

def unionlist(A, B):
    C = A.copy()
    for i in range(len(B)):
        flag1 = search(B[i],A)
        if flag1 == False:
            C.append(B[i])
    return C
    
def intersect(A, B):
    C = []
    for i in range(len(A)):
        flag = search(A[i],B)
        if flag:
            C.append(A[i])
    return C


def search(key, A):
    n = len(A)
    for i in range(n):
        if key == A[i]:
            flag = True
            return flag
    flag = False
    return flag
        
def sub(A, B):
    C = []
    for i in A:
        flag = search(i, B)
        if flag == False:
            C.append(i)
    return C
            
        
def main():
    Group_A = []
    Group_B = []
    Group_C = []
    ansl = []

    while True:
        print("1 - Accept Information")
        print("2 - List of Students who play both Cricket and Badminton ")
        print("3 - List of Students who play either Cricket or Badminton but not both ")
        print("4 - List of Students who play neither Cricket or Badminton ")
        print("5 - Number of Students who play Cricket and Football but not Both ")
        print("6 - Exit ")

        ch = int(input("Enter your Choice"))

        if (ch == 1):
            accept_data(Group_A , "Cricket")
            show_data(Group_A , "Cricket")

            accept_data(Group_B , "Badminton")
            show_data(Group_B , "Badminton")

            accept_data(Group_C , "Football")
            show_data(Group_C , "Football")

        elif (ch == 2):
            ansl = intersect(Group_A, Group_B)

            if ansl == []:
                print("No such students present!")
            else:
                print("Answer: List of Students who play both Cricket and Badminton is - ", ansl)
            
        elif (ch == 3):
            temp1 = []
            temp2 = []

            temp1 = unionlist(Group_A, Group_B)
            temp2 = intersect(Group_A, Group_B)
            ansl = sub(temp1,temp2)

            if ansl == []:
                print("No such Students present!")
            else:
                print("Answer: List of Students who play either Cricket or Badminton but not both - ", ansl)
        
        elif (ch == 4):
            all = unionlist(unionlist(Group_A, Group_B), Group_C)
            ansl = sub(all,unionlist(Group_A, Group_B))

            if ansl == []:
                print("No such students present!")
            else:
                print("Answer: List of Students who play neither Cricket or Badminton - ", ansl)


        elif (ch == 5):
            temp1 = []
            temp2 = []

            temp1 = unionlist(Group_A, Group_C)
            temp2 = intersect(Group_A, Group_C)
            ansl = sub(temp1,temp2)
            num = len(ansl)

            if ansl == []:
                print("No such Students present!")
            else:
                print("Answer: Number of Students who play Cricket and Football but not Both - ", num)


        elif (ch == 6):
            print("End of Program!!")
            break


        else:
            print("Wrong Choice entered!!")


main()








