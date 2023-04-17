import java.util.Scanner;

public class Questao2 {
    private Scanner sc = new Scanner(System.in);
    private int matriz[][] = new int[6][6];
    private boolean encontrado = false;
    private int x;

    //Construtor
    Questao2() {
        for (int i = 0; i < 6; i++)
            for (int j = 0; j < 6; j++)
                this.matriz[i][j] = this.sc.nextInt();
        this.x = sc.nextInt();
    }

    //Métodos
    public void procuraElemento() {
        for (int i = 0; i < 6; i++)
            if (this.encontrado == true)
                break;
            else
                for (int j = 0; j < 6; j++)
                    if (this.matriz[i][j] == this.x) {
                        System.out.println(String.format("Encontrado! M[%d][%d]", i, j));
                        this.encontrado = true;
                        break;
                    }
        if (this.encontrado == false)
            System.out.println("Não Encontrado!");
    }

    //Main
    public static void main(String[] args) {
        Questao2 objeto = new Questao2();
        objeto.procuraElemento();
    }
}
