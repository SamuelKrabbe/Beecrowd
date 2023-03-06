import java.util.Scanner;

public class prob_1005 {
    public static void main(String[] args){
        double media;
        Scanner entrada = new Scanner(System.in);
        double a = entrada.nextDouble();
        double b = entrada.nextDouble();
        entrada.close();
        
        media = (a * 3.5 + b * 7.5) / 11;
        String resultado = String.format("%.5f", media);
        System.out.println("MEDIA = " + resultado);
    }
}
