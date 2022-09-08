#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int column;
    char operation;
    float matriz[12][12], soma = 0.0, media;

    scanf("%d", &column);
    scanf("%c", &operation);

    for (int i = 0; i < 12; i++)
    {
        for (int j = 0; j < 12; j++)
        {
            scanf("%f", &matriz[i][j]);
        }
    }
    for (int k = 0; k < 12; k++)
    {
        soma += matriz[k][column];
    }

    if (operation == 'M')
    {
        media = soma / 12.0;
        printf("%.1f\n", media);
    }
    else
    {
        printf("%.1f\n", soma);
    }
    return 0;
}
