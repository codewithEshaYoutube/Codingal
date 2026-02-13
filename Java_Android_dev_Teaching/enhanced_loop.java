int sum = numbers.stream()
                 .filter(n -> n % 2 == 0)
                 .peek(System.out::println)
                 .mapToInt(Integer::intValue)
                 .sum();

System.out.println("Sum = " + sum);
