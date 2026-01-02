class Main{
    public static void main(String[] args){
        int a=10;
        int b=13;
        //Method 
        int sum=a+b;
        int diff=a-b;
        int multiply=a*b;
        int div= a/b;
        int rem=a%b;
        System.out.println("========Method 1======");
        System.out.println("addition of a & b ="+sum);
        System.out.println("subtraction of a & b ="+diff);
        System.out.println("multiplication of a & b =" + multiply);
        System.out.println("division of a & b ="+ div);
        System.out.println("remainder of a & b ="+rem);
        
        System.out.println();
        System.out.println("========Method 2======");
        System.out.println("addition of a & b ="+(a+b));
        System.out.println("subtraction of a & b ="+(a-b));
        System.out.println("multiplication of a & b =" + (a*b));
        System.out.println("division of a & b ="+ (a/b));
        System.out.println("remainder of a & b ="+(a%b));
        
        System.out.println();
        System.out.println("========Method 3======");
        System.out.println("addition of a & b ="+(a+b)+
        "subtraction of a & b ="+(a-b)+
        "multiplication of a & b =" + (a*b)+
        "division of a & b ="+ (a/b)+
        "remainder of a & b ="+(a%b));
        
        System.out.println();
        
    }
}