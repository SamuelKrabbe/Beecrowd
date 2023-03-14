import java.util.Scanner;

public class prob_1020 {
    public static void main(String[] args){
        int idadeEmDias, idadeEmMeses, idadeEmAnos;
        Scanner sc = new Scanner(System.in);

        idadeEmDias = sc.nextInt();

        if (idadeEmDias >= 365){
            idadeEmAnos = idadeEmDias / 365;
            idadeEmDias = idadeEmDias % 365;
            System.out.println(idadeEmAnos + " ano(s)");
        }
        else{
            System.out.println("0 ano(s)");
        }

        if (idadeEmDias >= 30){
            idadeEmMeses = idadeEmDias / 30;
            idadeEmDias = idadeEmDias % 30;
            System.out.println(idadeEmMeses + " mes(es)");
        }
        else{
            System.out.println("0 mes(es)");
        }

        System.out.println(idadeEmDias + " dia(s)");
        sc.close();
    }
}
