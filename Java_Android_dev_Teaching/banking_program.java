/*
banking app program
*/
import java.util.*;

public class BankApp {
    static  Scanner sc= new Scanner (System.in);//input   builtin function
    static Map <String,Double>accounts=new HashMap<>(); // data structure
    public static void main(String args[]) {
        //conditional
    while(true){
        System.out.println("\n-1.Add customer");
        System.out.println("\n-2.Check Balance");
        System.out.println("\n-3.Withdraw/Deposit");
        System.out.println("\n-4.Exit");
        System.out.println("\n choose option");
        
    
        int choice = sc.nextInt(); // get the input as integers
        sc.nextLine();
        switch(choice){
            case 1->addCustomer();
            case 2->checkbalance();
            case 3->updatebalance();
            case 4->{
                System.out.println("Goodbye");
                return;
            }
            
           
            default -> System.out.println("Your choice is invalid");
                }
            }
        }
     static void addCustomer(){
    System.out.println(" Enter your name ");
    String name=sc.nextLine();
    System.out.println(" enter your intial/opening  balance: ");
    double balance =sc.nextDouble();
    accounts.put(name,balance);
    System.out.print(" Account created ");
    
}
 static void checkbalance(){
    System.out.println(" Enter your name ");
    String name=sc.nextLine();
    if(accounts.containsKey(name)){
        System.out.println("Balance;"+accounts.get(name));
        
        
    }else{
        
        System.out.println(" User not found ");
    }
    
    
    
}
 static void updatebalance(){
    System.out.println(" Enter your name ");
    String name=sc.nextLine();
    if(accounts.containsKey(name)){
        System.out.println("Enter your amount(deposit/withdraw): ");
        double amount=sc.nextDouble();
        accounts.put(name,accounts.get(name)+amount);
        System.out.println("successful transaction ");
    
        
        
    }else{
        
        System.out.println(" User not found ");
    }
    
    
    
}

}
  

        
    
      
      
      
    
