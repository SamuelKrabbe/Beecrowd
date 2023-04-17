import java.util.Scanner;

abstract class Poligono {
    private String nome;
    private int numLados;

    //Construtor
    Poligono(String nome, int numLados) {
        this.nome = nome;
        this.numLados = numLados;
    }

    //Métodos
        //Getters & Setters
        public String getNome() {
            return this.nome;
        }

        public void setNome(String nome) {
            this.nome = nome;
        }

        public int getNumLados() {
            return this.numLados;
        }

        public void setNumLados(int numLados) {
            this.numLados = numLados;
        }
}   

public class Quadrado extends Poligono {
    private double lado;

    //Construtor
    Quadrado(String nome, int numLados, double lado) {
        super(nome, numLados);
        this.lado = lado;
    }

    //Métodos
        //Getters & Setters
        public double getLado() {
            return this.lado;
        }

        public void setLado(double lado) {
            this.lado = lado;
        }

    public double area() {
        double area = this.lado * this.lado;
        return area;
    }

    @Override
    public String toString() {
        return super.getNome() + " tem " + super.getNumLados() + " lados e área= " + area();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String nome;
        int numLados;
        double lado;

        nome = sc.next();
        numLados = sc.nextInt();
        lado = sc.nextDouble();

        Quadrado quadrado = new Quadrado(nome, numLados, lado);
        System.out.println(quadrado);

        lado = sc.nextDouble();
        quadrado.setLado(lado);
        System.out.println(quadrado);
    }
}
