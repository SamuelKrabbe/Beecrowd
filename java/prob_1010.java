import java.text.DecimalFormat;
import java.util.Scanner;

public class prob_1010 {
    public static void main(String[] args){
        int codigo, numUnidades;
        float precoUnidade, totalPagar;
        totalPagar = 0.00F;
        Scanner sc = new Scanner(System.in);
        DecimalFormat df = new DecimalFormat("0.00");

        for (int i = 0; i < 2; i++){
            codigo = sc.nextInt();
            numUnidades = sc.nextInt();
            precoUnidade = sc.nextFloat();
            totalPagar += (numUnidades * precoUnidade);
        }

        System.out.println("VALOR A PAGAR: R$ " + df.format(totalPagar));
        sc.close();
    }
}
