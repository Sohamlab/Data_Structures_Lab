import java.util.Scanner;

class Main {
    
    public static boolean is_same_digit(int a, int b){
    if(a < 0 || b < 0){
      return false;
    }
    else if(a%10 == b%10){
      return true;
    }
    else{
    return false;
    }
  }
  
    public static void main(String[] args) {
        System.out.println("Enter the Two numbers to be checked: ");
        Scanner obj = new Scanner(System.in);
        int num1 = obj.nextInt();
        int num2 = obj.nextInt();
        System.out.println(is_same_digit(num1,num2));
    }
}
