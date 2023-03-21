import java.util.Scanner;

public class prob_1064 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        float valor, soma, media;
        int positivos;
        soma = 0.0f;
        positivos = 0;

        for (int i = 0; i < 6; i++){
            valor = sc.nextFloat();

            if (valor > 0){
                soma += valor;
                positivos++;
            }
        }
        media = soma / positivos;

        System.out.println(positivos + " valores positivos");
        System.out.println(String.format("%.1f", media));

        sc.close();
    }
}
