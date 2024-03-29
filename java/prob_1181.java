import java.util.Scanner;

public class prob_1181 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int linha, x = 12;
        char op;
        double m[][] = new double[x][x];
        double soma = 0;

        linha = sc.nextInt();
        op = sc.next().toUpperCase().charAt(0);

        for (int i = 0; i < x; i++){
            for (int j = 0; j < x; j++){
                m[i][j] = sc.nextDouble();
            }
        }

        for (int k = 0; k < x; k++)
            soma += m[linha][k];

        switch (op){
            case 'S':
                System.out.println(String.format("%.1f", soma));
                break;
            case 'M':
                System.out.println(String.format("%.1f", soma / x));
                break;
            default:
                break;
        }

        sc.close();
    }
}
