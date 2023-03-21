import java.util.Scanner;

public class prob_1073 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int valor, quadrado;

        valor = sc.nextInt();

        for (int i = 1; i <= valor; i++){
        
            if (i % 2 == 0){
                quadrado = i * i;
                System.out.println(i + "^2 = " + quadrado);
            }
        }
        sc.close();
    }
}
