import java.util.Scanner;

public class prob_1172 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int x[] = new int[10];

        for (int i = 0; i < 10; i++){
            x[i] = sc.nextInt();

            if (x[i] <= 0)
                x[i] = 1;
        }

        for (int j = 0; j < 10; j++)
            System.out.println(String.format("X[%d] = %d", j, x[j]));
        sc.close();
    }
}
