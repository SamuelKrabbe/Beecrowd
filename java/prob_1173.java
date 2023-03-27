import java.util.Scanner;

public class prob_1173 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int n[] = new int[10];

        n[0] = sc.nextInt();

        for (int i = 1; i < 10; i++)
            n[i] = n[i - 1] * 2;

        for (int j = 0; j < 10; j++)
            System.out.println(String.format("N[%d] = %d", j, n[j]));
        sc.close();
    }
}
