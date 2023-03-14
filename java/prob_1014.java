import java.util.Scanner;

public class prob_1014 {
    public static void main(String[] args){
        int distanciaTotal;
        float gasolinaTotal, consumoMedio;
        Scanner sc = new Scanner(System.in);

        distanciaTotal = sc.nextInt();
        gasolinaTotal = sc.nextFloat();

        consumoMedio = distanciaTotal / gasolinaTotal;

        System.out.println(String.format("%.3f km/l", consumoMedio));

        sc.close();
    }
}
