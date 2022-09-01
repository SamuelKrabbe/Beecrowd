#include <stdio.h>
#include <stdlib.h>

int main() {
    int even[5], odd[5], aux, vetorSizeEven = 0, vetorSizeOdd = 0;

    for(int i = 0; i < 15; i++){
        scanf("%d", &aux);

        if(aux % 2 == 0){
            even[vetorSizeEven] = aux;
            vetorSizeEven++;

            if(vetorSizeEven == 5){
                for(int j = 0; j < 5; j++){
                    printf("par[%d] = %d\n", j, even[j]);
                }
                vetorSizeEven = 0;
            }
        }else{
            odd[vetorSizeOdd] = aux;
            vetorSizeOdd++;

            if(vetorSizeOdd == 5){
                for(int k = 0; k < 5; k++){
                    printf("impar[%d] = %d\n", k, odd[k]);
                }
                vetorSizeOdd = 0;
            }
        }
    }

    for(int m = 0; m < vetorSizeOdd; m++){
        printf("impar[%d] = %d\n", m, odd[m]);
    }
    for(int n = 0; n < vetorSizeEven; n++){
        printf("par[%d] = %d\n", n, even[n]);
    }
    
    return 0;
}
