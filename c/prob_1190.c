#include <stdio.h>
#include <stdlib.h>

float sumOfRightsideMatrix(float matriz[12][12])
{
    float sum = 0;
    int x = 1;

    for (int column = 11; column > 6; column--)
    {
        for (int row = x; row < column; row++)
        {
            sum += matriz[row][column];
        }
        x++;
    }
    return sum;
}

int main()
{
    char sumOrAverage;
    float sum, average, matriz[12][12];

    scanf("%c\n", &sumOrAverage);

    for (int i = 0; i < 12; i++)
    {
        for (int j = 0; j < 12; j++)
        {
            scanf("%f\n", &matriz[i][j]);
        }
    }

    sum = sumOfRightsideMatrix(matriz);

    if (sumOrAverage == 'M')
    {
        average = sum / 30;
        printf("%.1f\n", average);
    }
    else
    {
        printf("%.1f\n", sum);
    }
    return 0;
}
