import java.util.Scanner;

public class prob_1038{
    public static void main(String[] args){
        int codigo, quantidade;
        double preco;
        Scanner sc = new Scanner(System.in);

        codigo = sc.nextInt();
        quantidade = sc.nextInt();

        switch(codigo){
            case 1:
                preco = quantidade * 4.00;
                System.out.println(String.format("Total: R$ %.2f", preco));
                break;
            case 2:
                preco = quantidade * 4.50;
                System.out.println(String.format("Total: R$ %.2f", preco));
                break;
            case 3:
                preco = quantidade * 5.00;
                System.out.println(String.format("Total: R$ %.2f", preco));
                break;
            case 4:
                preco = quantidade * 2.00;
                System.out.println(String.format("Total: R$ %.2f", preco));
                break;
            case 5:
                preco = quantidade * 1.50;
                System.out.println(String.format("Total: R$ %.2f", preco));
                break;
            default:
                System.out.println("Código Inválido");
                break;
        }
        
        sc.close();
    }
}