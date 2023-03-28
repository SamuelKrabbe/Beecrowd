import java.util.Scanner;

public class prob_1183 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int x = 12, count = 0;
        char op;
        double m[][] = new double[x][x];
        double soma = 0;

        op = sc.next().toUpperCase().charAt(0);

        for (int i = 0; i < x; i++) {
            for (int j = 0; j < x; j++) {
                m[i][j] = sc.nextDouble();
            }
        }

        for (int k = 0; k < x - 1; k++){
            for (int p = k + 1; p < x; p++){
                soma += m[k][p];
                count++;
            }
        }

        switch (op) {
            case 'S':
                System.out.println(String.format("%.1f", soma));
                break;
            case 'M':
                System.out.println(String.format("%.1f", soma / count));
                break;
            default:
                break;
        }

        sc.close();
    }
}
