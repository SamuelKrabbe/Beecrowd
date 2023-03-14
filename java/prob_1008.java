import java.text.DecimalFormat;
import java.util.Scanner;

public class prob_1008 {
    public static void main(String[] args){
        int num, salarioHora;
        float horasTrabalhadas, salario;
        Scanner sc = new Scanner(System.in);
        DecimalFormat df = new DecimalFormat("0.00");

        num = sc.nextInt();
        salarioHora = sc.nextInt();
        horasTrabalhadas = sc.nextFloat();

        salario = salarioHora * horasTrabalhadas;

        System.out.println("NUMBER = " + num);
        System.out.println("SALARY = U$ " + df.format(salario));
        sc.close();
    }
}
