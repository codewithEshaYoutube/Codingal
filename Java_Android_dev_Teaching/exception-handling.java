// Exception Handling
// try catch

import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner input =new Scanner(System.in);
        try{
        System.out.println("Enter your name  ");
        String name= input.nextLine();
        if (name.matches("\\d+")) {   // conditional 
        throw new Exception("Name cannot be only numbers");
    }
      
        System.out.println("Hi "+name+" How can I help you ");

           }
        catch(Exception e ){   //event
            System.out.println("This is invalid input please enter your name in alphabets");
        }
        finally{
            input.close();
            System.out.println("Program is finished");
            
        }
    }
}

