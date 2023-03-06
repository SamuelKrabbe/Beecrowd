import java.util.Scanner;

public class prob_1001 {
    public static void main(String[] args){
        int soma;
        Scanner entrada = new Scanner(System.in);
        int a = entrada.nextInt();
        int b = entrada.nextInt();
        entrada.close();
        
        soma = a + b;
        System.out.println("X = " + soma);
    }
}
