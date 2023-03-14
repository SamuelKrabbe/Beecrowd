import java.util.Scanner;

public class prob_1016 {
    public static void main(String[] args){
        int distancia, tempo;
        Scanner sc = new Scanner(System.in);

        distancia = sc.nextInt();
        tempo = distancia * 2;

        System.out.println(tempo + " minutos");
        sc.close();
    }
}
