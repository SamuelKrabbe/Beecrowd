import java.util.Scanner;

public class prob_1174 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        float a[] = new float[100];

        for (int i = 0; i < 100; i++)
            a[i] = sc.nextFloat();

        for (int j = 0; j < 100; j++)
            if (a[j] <= 10)
                System.out.println(String.format("A[%d] = %.1f", j, a[j]));

        sc.close();
    }
}
