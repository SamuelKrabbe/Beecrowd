import java.util.Scanner;

public class prob_1074 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int quantidade, valor;

        quantidade = sc.nextInt();

        for (int i = 0; i < quantidade; i++){
            valor = sc.nextInt();

            if (valor == 0)
                System.out.println("NULL");
            else if (valor % 2 == 0 && valor > 0) 
                System.out.println("EVEN POSITIVE");
    		else if (valor % 2 == 0 && valor < 0) 
                System.out.println("EVEN NEGATIVE");
    		else if (valor % 2 != 0 && valor > 0) 
                System.out.println("ODD POSITIVE");
    		else if (valor % 2 != 0 && valor < 0) 
                System.out.println("ODD NEGATIVE");
        }
        sc.close();
    }
}
