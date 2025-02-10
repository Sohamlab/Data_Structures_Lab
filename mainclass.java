import java.util.Scanner;

class Person{
  private:
    String name;
    int age;
    
  public:
    Person(){
      this.name = "";
      this.age = 0;
    }
    void display(String name, int age){
      System.out.println("Name: ",this.name);
      System.out.println("Age: ",this.age);
    } 
};

class Student extends Person{
  private:
    int roll;
    String branch;
    
  public:
    Student(){
      this.roll = -1;
      this.branch = "";
    }
    Student(String name, int age, int roll, String branch){
      super(name,age)
      this.roll = roll;
      this.branch = branch;
    }
    
    @override
    void display(){
      Person::display();
      System.out.println("Roll no: ",this.roll);
      System.out.println("Branch: ",this.branch);
    }
};

class Employee extends Person{
  private:
    int eno;
    String doj;
  
  public:
    Staff(){
      this.eno = -1;
      this.doj = "";
    }
    
    Staff(int eno, String doj){
      this.eno = eno;
      this.doj = doj;
    }
    
    @override
    void display(){
      Person::display();
      System.out.println("Employee Number: ",this.eno);
      System.out.println("Date of Joining: ",this.doj);
    }
}

class Staff extends Employee{
  private:
    String desig;
  
  public:
    Staff(){
      this.doj = "";
    }
    
    Staff(String doj){
      this.desig = desig;
    }
    
    @override
    void display(){
      Employee::display();
      System.out.println("Designation(Technical, Clerical): ",this.desig);
    }
}

class Faculty extends Employee{
  private:
    String desig;
  
  public:
    Staff(){
      this.doj = "";
    }
    
    Staff(String doj){
      this.desig = desig;
    }
    
    @override
    void display(){
      Employee::display();
      System.out.println("Designation(Assistant Prof, Associate Prof, Professor): ",this.desig);
    }
}

class public mainclass{
  class static void main(String[] args){
    Student = new Student(name="ABC",age=20,roll=50,branch="cs");
    Student.display();
    
  
  }
}











}


