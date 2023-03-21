import java.util.Scanner;

public class prob_1048 {
    public static void main(String[] args){
        float percentual;
        int percentualInt;
        double salario, reajuste;
        Scanner sc = new Scanner(System.in);

        salario = sc.nextDouble();

        if (salario >= 0 && salario <= 400){
            percentual = 0.15f;
            reajuste = salario * percentual;
            salario = salario * (1 + percentual);
            percentualInt = 15;
        }
        else{
            if (salario >= 400.01 && salario <= 800){
                percentual = 0.12f;
                reajuste = salario * percentual;
                salario = salario * (1 + percentual);
                percentualInt = 12;
            }
            else{
                if (salario >= 800.01 && salario <= 1200){
                    percentual = 0.10f;
                    reajuste = salario * percentual;
                    salario = salario * (1 + percentual);
                    percentualInt = 10;
                }
                else{
                    if (salario >= 1200.01 && salario <= 2000){
                        percentual = 0.07f;
                        reajuste = salario * percentual;
                        salario = salario * (1 + percentual);
                        percentualInt = 7;
                    }
                    else{
                        percentual = 0.04f;
                        reajuste = salario * percentual;
                        salario = salario * (1 + percentual);
                        percentualInt = 4;
                    }
                }
            }
        }

        
        System.out.println(String.format("Novo salario: %.2f", salario));
        System.out.println(String.format("Reajuste ganho: %.2f", reajuste));
        System.out.println("Em percentual: " + percentualInt + " %");

        sc.close();
    }
}
