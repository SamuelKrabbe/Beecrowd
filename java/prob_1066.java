import java.util.Scanner;

public class prob_1066 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        float valor;
        int pares, impares, positivos, negativos;
        pares = 0;
        impares = 0;
        positivos = 0;
        negativos = 0;

        for (int i = 0; i < 5; i++){
            valor = sc.nextFloat();

            if (valor % 2 == 0)
                pares++;
            if (valor % 2 != 0)
                impares++;
            if (valor > 0)
                positivos++;
            if (valor < 0)
                negativos++;
        }

        System.out.println(pares + " valor(es) par(es)");
        System.out.println(impares + " valor(es) impar(es)");
        System.out.println(positivos + " valor(es) positivo(s)");
        System.out.println(negativos + " valor(es) negativo(s)");

        sc.close();
    }
}
