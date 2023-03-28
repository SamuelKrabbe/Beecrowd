import java.util.Scanner;

public class prob_1180 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int menor, indice;
        int n = sc.nextInt();
        int x[] = new int[n];

        x[0] = sc.nextInt();
        menor = x[0];
        indice = 0;

        for (int i = 1; i < n; i++){
            x[i] = sc.nextInt();
            
            if (x[i] < menor){
                menor = x[i];
                indice = i;
            }
        }
         
        System.out.println("Menor valor: " + menor);
        System.out.println("Posicao: " + indice);

        sc.close();
    }
}
