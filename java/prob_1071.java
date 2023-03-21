import java.util.Scanner;

public class prob_1071 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int x, y, soma, aux;
        soma = 0;
        x = sc.nextInt();
        y = sc.nextInt();

        if (x > y){
            aux = x;
            x = y;
            y = aux;
        }

        for (int i = x + 1; i < y; i++){

            if (i % 2 != 0)
                soma += i;
        }

        System.out.println(soma);

        sc.close();
    }
}
