import geometry.Area;
import java.util.Scanner;

public class shape implements Area{
  @Override
  public double areaRectangle(double length, double breadth){
    return length*breadth;
  }
  
  @Override
  public double areaCircle(double radius){
    return Math.PI*radius*radius;
  }
  
}

