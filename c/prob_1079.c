#include <stdio.h>
#include <stdlib.h>

int main()
{

    int casosDeTeste;
    float valor1, valor2, valor3, mediaPonderada;
    scanf("%d", &casosDeTeste);

    for (int i = 0; i < casosDeTeste; i++)
    {
        scanf("%f %f %f", &valor1, &valor2, &valor3);

        mediaPonderada = ((valor1 * 2) + (valor2 * 3) + (valor3 * 5)) / 10;

        printf("%.1f\n", mediaPonderada);
    }

    return 0;
}