import java.util.Scanner;

public class prob_1043{
    public static  void main(String[] args){
        float a, b, c, perimeter, area;
        boolean isTri;
        Scanner sc = new Scanner(System.in);

        a = sc.nextFloat();
        b = sc.nextFloat();
        c = sc.nextFloat();
        
        perimeter = a + b + c;
        area = ((a + b) * c) / 2;

        if ((a + b <= c) || (a + c <= b) || (b + c <= a))
            isTri = false;
        else
            isTri = true;
            
        if (isTri)
            System.out.println(String.format("Perimetro = %.1f", perimeter));
        else
            System.out.println(String.format("Area = %.1f", area));
        sc.close();
    }
}