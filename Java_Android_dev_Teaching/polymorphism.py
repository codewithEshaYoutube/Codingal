class Shape {
    double area() {
        return 0;
    }
}

class Rectangle extends Shape {
    double l = 5, w = 4;

    double area() {          // overriding
        return l * w;
    }
}

class Triangle extends Shape {
    double b = 6, h = 3;

    double area() {          // overriding
        return 0.5 * b * h;
    }
}

class Main {
    public static void main(String[] args) {

        Shape s;             // parent reference

        s = new Rectangle(); // polymorphism
        System.out.println(s.area());

        s = new Triangle();  // polymorphism
        System.out.println(s.area());
    }
}
