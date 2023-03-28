import java.util.Scanner;

public class prob_1175 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int n[] = new int[20];
        int aux;

        for (int i = 0; i < 20; i++)
            n[i] = sc.nextInt();

        for (int j = 0, k = 19; j < 10 && k >= 10; j++, k--){
            aux = n[j];
            n[j] = n[k];
            n[k] = aux;
        }
         
        for (int p = 0; p < 20; p++){
            System.out.println(String.format("N[%d] = %d", p, n[p]));
        }

        sc.close();
    }
}
