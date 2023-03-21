import java.util.Scanner;

public class prob_1065 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        float valor;
        int pares;
        pares = 0;

        for (int i = 0; i < 5; i++){
            valor = sc.nextFloat();

            if (valor % 2 == 0)
                pares++;
        }

        System.out.println(pares + " valores pares");

        sc.close();
    }
}
