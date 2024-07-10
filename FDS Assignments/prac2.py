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


/*def accept_data(A):
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
            if  (A[i] == A[j] and A[i] != -1):
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
*/

(base) tpo@tpo-Vostro-3900:~/Desktop$ python3 prac2.py
1 - Accept Information
2 - The Average Score of the Class 
3 - Highest Score and Lowest Score of the Class 
4 - Count of Students who were Absent for the Test 
5 - Display Marks with Highest Frequency 
6 - Exit
Enter your Choice number: 10
Invalid Option!!
1 - Accept Information
2 - The Average Score of the Class 
3 - Highest Score and Lowest Score of the Class 
4 - Count of Students who were Absent for the Test 
5 - Display Marks with Highest Frequency 
6 - Exit
Enter your Choice number: 1
Enter number of students: 10
Enter the Marks of student 1 : (Enter -1 if Absent)10
Enter the Marks of student 2 : (Enter -1 if Absent)20
Enter the Marks of student 3 : (Enter -1 if Absent)30
Enter the Marks of student 4 : (Enter -1 if Absent)50
Enter the Marks of student 5 : (Enter -1 if Absent)50
Enter the Marks of student 6 : (Enter -1 if Absent)-1
Enter the Marks of student 7 : (Enter -1 if Absent)-1
Enter the Marks of student 8 : (Enter -1 if Absent)60
Enter the Marks of student 9 : (Enter -1 if Absent)70
Enter the Marks of student 10 : (Enter -1 if Absent)80
Student's Marks list is as follows :
Marks of student 1 : 10
Marks of student 2 : 20
Marks of student 3 : 30
Marks of student 4 : 50
Marks of student 5 : 50
Marks of student 6 : Absent
Marks of student 7 : Absent
Marks of student 8 : 60
Marks of student 9 : 70
Marks of student 10 : 80
1 - Accept Information
2 - The Average Score of the Class 
3 - Highest Score and Lowest Score of the Class 
4 - Count of Students who were Absent for the Test 
5 - Display Marks with Highest Frequency 
6 - Exit
Enter your Choice number: 2
8 370
The Average Score of the Class is:  46.25
1 - Accept Information
2 - The Average Score of the Class 
3 - Highest Score and Lowest Score of the Class 
4 - Count of Students who were Absent for the Test 
5 - Display Marks with Highest Frequency 
6 - Exit
Enter your Choice number: 3
The Highest Score is:  80
The Lowest Score is:  10
1 - Accept Information
2 - The Average Score of the Class 
3 - Highest Score and Lowest Score of the Class 
4 - Count of Students who were Absent for the Test 
5 - Display Marks with Highest Frequency 
6 - Exit
Enter your Choice number: 4
The Number of Students Absent for the Test is :  2
1 - Accept Information
2 - The Average Score of the Class 
3 - Highest Score and Lowest Score of the Class 
4 - Count of Students who were Absent for the Test 
5 - Display Marks with Highest Frequency 
6 - Exit
Enter your Choice number: 5
The Marks with Highest Frequency of  2 are:  50
1 - Accept Information
2 - The Average Score of the Class 
3 - Highest Score and Lowest Score of the Class 
4 - Count of Students who were Absent for the Test 
5 - Display Marks with Highest Frequency 
6 - Exit
Enter your Choice number: 6
End of Program!!

matt add
//Program to take a 2-D array from user and display the 2-D array: 
#include <iostream>
using namespace std;

int main(){
  int row_num, col_num,i,j;
  
  cout<<"Give the number of Rows in 2D Matrix: ";
  cin>>row_num;
  cout<<"Give the number of Columns in 2D Matrix: ";
  cin>>col_num;
  
  int arr[row_num][col_num];
  for (i=0; i<row_num; i++){
    for (j=0; j<col_num; j++){
      cout<<"Give the "<<i<<" rows "<<j<<" element: ";
      cin>>arr[i][j];
     }
   }
   //Display
   for (i=0; i<row_num; i++){
    for (j=0; j<col_num; j++){
      cout<<arr[i][j];
     }
     cout<<endl;
   }
     



  return 0;
}


matt add cpp

/Program to take 2, 2-D array from user and display the Addition array: 
#include <iostream>
using namespace std;

int main(){
int row_num, col_num,i,j,sum=0;
  
  cout<<"Give the number of Rows in 2D Matrix: ";
  cin>>row_num;
  cout<<"Give the number of Columns in 2D Matrix: ";
  cin>>col_num;
  
  int arr1[row_num][col_num];
  for (i=0; i<row_num; i++){
    for (j=0; j<col_num; j++){
      cout<<"Give the "<<i<<" rows "<<j<<" element: ";
      cin>>arr1[i][j];
     }
   }
     
  int arr2[row_num][col_num];
  for (i=0; i<row_num; i++){
    for (j=0; j<col_num; j++){
      cout<<"Give the "<<i<<" rows "<<j<<" element: ";
      cin>>arr2[i][j];
     }
   }
  int add_arr[row_num][col_num];
  for (i=0; i<row_num; i++){
    for (j=0; j<col_num; j++){
      sum = arr1[i][j] + arr2[i][j];
      add_arr[i][j] = sum;
      sum = 0;
      }
    }
    
  for (i=0; i<row_num; i++){
    for (j=0; j<col_num; j++){
      cout<<add_arr[i][j];
     }
     cout<<endl;
   }
  return 0;
 }
      
      
  matt sum



