import java.util.Scanner;

public class problem5{
  public static void main(String[] args){
    Scanner obj = new Scanner(System.in);
    System.out.println("Enter the size of Array: ");
    int size = obj.nextInt();
    int arr[] = new int[size];
    
    System.out.println("Enter the Elements of Array: ");
    for(int i=0; i<size; i++){
      arr[i] = obj.nextInt();
    }
    System.out.println("Array elements are: ");
    for(int i=0; i<size; i++){
      System.out.println(arr[i]);
    }
    
    int temp = arr[0];
    arr[0] = arr[size-1];
    arr[size-1] = temp;
    
    System.out.println("After Swapping First and Last element Array elements are: ");
    for(int i=0; i<size; i++){
      System.out.println(arr[i]);
    }
    
    obj.close();
  }
}
