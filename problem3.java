import java.util.Scanner;
public class Main {
    
    public static void xylem_phloem(int num) {
        String num_str = Integer.toString(num);
        int n = num_str.length();
        int sum_ext = Integer.parseInt(String.valueOf(num_str.charAt(0))) + Integer.parseInt(String.valueOf(num_str.charAt(n-1)));
        int sum_mean = 0;
        for (int i = 1; i < n - 1; i++) {
            sum_mean += Integer.parseInt(String.valueOf(num_str.charAt(i)));
        }
        if (sum_ext == sum_mean) {
            System.out.println("The given number is a Xylem number");
        } else {
            System.out.println("The given number is a Phloem number");
        }
    }

    public static void main(String[] args) {
        System.out.println("Enter the number to be checked: ");
        Scanner obj = new Scanner(System.in);
        int num = obj.nextInt();
        xylem_phloem(num);
    }
}

