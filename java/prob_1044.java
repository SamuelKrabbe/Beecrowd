import java.util.Scanner;

public class prob_1044 {
    public static void main(String[] args){
        int a, b, resto;
        Scanner sc = new Scanner(System.in);

        a = sc.nextInt();
        b = sc.nextInt();

        if (a > b)
            resto = a % b;
        else
            resto = b % a;

        if (resto == 0)
            System.out.println("Sao Multiplos");
        else
            System.out.println("Nao sao Multiplos");
        sc.close();
    }
}
