import java.util.Scanner;

public class prob_1435 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

    	int tamanhoMat = sc.nextInt();
    	int aux;

    	while (tamanhoMat != 0) {
    		for (int coluna = 1; coluna <= tamanhoMat; coluna++) {
    			for (int linha = 1 ; linha <= tamanhoMat; linha++) {
    				aux = coluna;

                    if (linha < aux) 
                        aux = linha;
                    if (tamanhoMat - coluna + 1 < aux) 
                        aux = tamanhoMat - coluna + 1;
                    if (tamanhoMat - linha + 1 < aux) 
                        aux = tamanhoMat - linha + 1;
                    
                    System.out.printf("%3d", aux);

                    if (linha < tamanhoMat) 
                        System.out.print(" ");
                    else 
                        System.out.print("\n");
                }
            }
            System.out.print("\n");
            tamanhoMat = sc.nextInt();
        }
    

        sc.close();
    }
}
