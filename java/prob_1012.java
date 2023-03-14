import java.text.DecimalFormat;
import java.util.Scanner;

public class prob_1012 {
    public static void main(String[] args){
        double a, b, c, tria, circ, trap, quad, ret, pi;
        pi = 3.14159F;
        Scanner sc = new Scanner(System.in);
        DecimalFormat df = new DecimalFormat("0.000");

        a = sc.nextDouble();
        b = sc.nextDouble();
        c = sc.nextDouble();

        tria = (a * c) / 2.0;
        circ = pi * (c * c);
        trap = ((a + b) * c) / 2.0;
        quad = b * b;
        ret = a * b;

        System.out.println("TRIANGULO: " + df.format(tria));
        System.out.println("CIRCULO: " + df.format(circ));
        System.out.println("TRAPEZIO: " + df.format(trap));
        System.out.println("QUADRADO: " + df.format(quad));
        System.out.println("RETANGULO: " + df.format(ret));
        sc.close();
    }
}
