import java.util.Scanner;

public class Teste {

    //Construtor
    Teste() {
    }

    //Métodos

    //Main
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String estadio;
        double valArquib;
        double valCadeira;
        int maxArquib;
        int maxCadeira;
        int quantIngressosArq;
        int quantIngressosCad;

        estadio = sc.nextLine();
        valArquib = sc.nextDouble();
        valCadeira = sc.nextDouble();
        maxArquib = sc.nextInt();
        maxCadeira = sc.nextInt();
        quantIngressosArq = sc.nextInt();
        quantIngressosCad = sc.nextInt();

        Ingresso ingresso = new Ingresso(estadio, valArquib, valCadeira, maxArquib, maxCadeira);
        ingresso.comprarIngresos(quantIngressosArq, quantIngressosCad);
    }
}

class Ingresso {
    private String estadio;
    private double valArquib;
    private double valCadeira;
    private int maxArquib;
    private int maxCadeira;
    private double total = 0.0f;
    private boolean temArq = false;
    private boolean temCad = false;

    //Construtor
    Ingresso(String estadio, double valArquib, double valCadeira, int maxArquib, int maxCadeira) {
        this.estadio = estadio;
        this.valArquib = valArquib;
        this.valCadeira = valCadeira;
        this.maxArquib = maxArquib;
        this.maxCadeira = maxCadeira;
    }

    //Métodos
    void comprarIngresos(int qtdeArq,int qtdeCad) {
        if (qtdeArq <= maxArquib) {
            this.total += qtdeArq * this.valArquib;
            this.maxArquib -= qtdeArq;
            this.temArq = true;
        }

        if (qtdeCad <= maxCadeira) {
            this.total += qtdeCad * this.valCadeira;
            this.maxCadeira -= qtdeCad;
            this.temCad = true;
        }

        if (!temArq) {
            System.out.println("Não foi possível comprar na Arquibancada");
            
        }
        if (!temCad) {
            System.out.println("Não foi possível comprar nas Cadeiras");
        }
        
        System.out.println(String.format("Valor total dos ingressos: R$ %.1f", this.total));
        System.out.println(String.format("Ingressos disponíveis no %s", this.estadio));
        System.out.println(String.format("Arquibancada=%d lugares e cadeiras=%d lugares", this.maxArquib, this.maxCadeira));
    }
}
