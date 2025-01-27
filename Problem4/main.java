import geometry.Area;
import java.util.Scanner;

public class main{
  public static void main(String[] args){
    shape shape = new shape();
    Scanner obj = new Scanner(System.in);
    System.out.println("Enter the length of Rectangle: ");
    double length = obj.nextDouble();
    System.out.println("Enter the Breadth of Rectangle: ");
    double breadth = obj.nextDouble();
    System.out.println("Enter the Radius of Rectangle: ");
    double radius = obj.nextDouble();
    System.out.println("THe Area of rectangle is: ");
    System.out.println(shape.areaRectangle(length, breadth));
    System.out.println("THe Area of circle is: ");
    System.out.println(shape.areaCircle(radius));
  
  }
}
