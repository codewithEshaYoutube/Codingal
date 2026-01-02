// Online Java Compiler
// Use this editor to write, compile and run your Java code online

class Main {
    public static void main(String[] args) {
    
    System.out.println("different types of operators");
    System.out.println("Mind game");
    int a = 5;
    int b= 8;
    System.out.println("Guess the numbers");
    //uniary operators
    System.out.println("uniary operator"+(a++));
    System.out.println("uniary operator"+(++b));
    
    // binary operator
    System.out.println("Binary operator");
    System.out.println("1+2 = "+  (1+2));
    System.out.println("1*2 = "+  (1*2));
    System.out.println("1/2 = "+  (1/2));
    System.out.println("1-2 = "+  (1-2));
    int increment= ++a * b++;
    System.out.println(increment);
    System.out.println("current value of a "+a);
    System.out.println("current value of b "+b);
    //  ternary operators
    System.out.println("Ternary operator");
    int Largestnum=(a>b)?a:b;
    System.out.println("largest of 2 numbers is   " +Largestnum);

    
    }
}