import java.util.Scanner;

public class Questao1 {
    private Scanner sc = new Scanner(System.in);
    private int vetor[] = new int[10];

    //Construtor
    Questao1() {
        for (int i = 0; i < 10; i++)
            this.vetor[i] = this.sc.nextInt();
    }

    //Métodos
    public void trocaElementos() {
        for (int i = 0; i < 10; i++) {
            if (this.vetor[i] % 3 == 0 && this.vetor[i] >= 0) {
                this.vetor[i] = -3;
            }
        }
    }

    public void imprimeVetor() {
        for (int i = 0; i < 10; i++) {
            System.out.println(String.format("X[%d] = %d", i, this.vetor[i]));
        }
    }

    //Main
    public static void main(String[] args) {
        Questao1 objeto = new Questao1();
        objeto.trocaElementos();
        objeto.imprimeVetor();
    }
}
