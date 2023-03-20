import java.util.Scanner;

public class prob_1037{
    public static void main(String[] args){
        float num;
        Scanner sc = new Scanner(System.in);

        num = sc.nextFloat();

        if (num >= 0 && num <= 25)
            System.out.println("Intervalo [0,25]");
        if (num > 25 && num <= 50)
            System.out.println("Intervalo (25,50]");
        if (num > 50 && num <= 75)
            System.out.println("Intervalo (50,75]");
        if (num > 75 && num <= 100)
            System.out.println("Intervalo (75,100]");    
        if (num < 0 || num > 100)
            System.out.println("Fora de intervalo");    
        sc.close();
    }
}