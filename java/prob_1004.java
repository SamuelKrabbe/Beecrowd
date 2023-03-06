import java.util.Scanner;

public class prob_1004 {
    public static void main(String[] args){
        int produto;
        Scanner entrada = new Scanner(System.in);
        int a = entrada.nextInt();
        int b = entrada.nextInt();
        entrada.close();
        
        produto = a * b;
        System.out.println("PROD = " + produto);
    }
}
