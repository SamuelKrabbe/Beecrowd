import java.util.Scanner;

public class prob_1042{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int a, b, c;

        a = sc.nextInt();
        b = sc.nextInt();
        c = sc.nextInt();

        if ((a <= b) && (a <= c)){
            System.out.println(a);
            if (b <= c){
                System.out.println(b);
                System.out.println(c);
            }
            else{
                System.out.println(c);
                System.out.println(b);
            }
        }
        else{
            if ((b <= a) && (b <= c)){
                System.out.println(b);
                if (a <= c){
                    System.out.println(a);
                    System.out.println(c);
                }
                else{
                    System.out.println(c);
                    System.out.println(a);
                }
            }
            else{
                System.out.println(c);
                if (a <= b){
                    System.out.println(a);
                    System.out.println(b);
                }
                else{
                    System.out.println(b);
                    System.out.println(a);
                }
            }
        }

        System.out.println();
        System.out.println(a);
        System.out.println(b);
        System.out.println(c);

        sc.close();
    }
}