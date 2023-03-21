import java.util.Scanner;

public class prob_1072 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int quantidade, valor, dentro, fora;
        quantidade = sc.nextInt();
        dentro = 0;
        fora = 0;

        for (int i = 0; i < quantidade; i++){
            valor = sc.nextInt();
        
            if (valor >= 10 && valor <= 20)
                dentro++;
            else
                fora++;
        }

        System.out.println(dentro + " in");
        System.out.println(fora + " out");

        sc.close();
    }
}
