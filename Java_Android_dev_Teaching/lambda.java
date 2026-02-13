// lambda usage

import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        System.out.println("=========Lambdas========");
        ArrayList<Integer> numbers = new ArrayList<>();
        numbers.add(34);
        numbers.add(45);
        numbers.add(78);
        numbers.add(56);
        numbers.add(36);
        numbers.add(99);
        numbers.add(23);
        numbers.add(17);
        numbers.forEach(x -> System.out.println(x));
        numbers.forEach(n -> {
            if (n == 49)
                System.out.println("Found 49");
        });
    }
}

        //lambdas
    
