import java.util.Scanner;

class Main {
    
    public static int sum_3num(int a,int b,int c){
        int sum=0;
        if(a != 13){
            sum+=a;
            if(b != 13){
                sum+=b;
                if(c != 13){
                    sum+=c;
                }
                else{
                    return sum;
                }
            }
            else{
                return sum;
            }
        }
        else{
            return sum;
        }
        return sum;
    }
  
    public static void main(String[] args) {
        System.out.println("Enter the three numbers to be summed: ");
        Scanner obj = new Scanner(System.in);
        int num1 = obj.nextInt();
        int num2 = obj.nextInt();
        int num3 = obj.nextInt();
        System.out.println(sum_3num(num1,num2,num3));
    }
}
