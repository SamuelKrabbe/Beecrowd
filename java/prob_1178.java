import java.util.Scanner;

public class prob_1178 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        double n[] = new double[100];
        double x;

        x = sc.nextDouble();
        n[0] = x;

        for (int i = 1; i < 100; i++)
            n[i] = n[i - 1] / 2;
         
        for (int j = 0; j < 100; j++){
            System.out.println(String.format("N[%d] = %.4f", j, n[j]));
        }

        sc.close();
    }
}
