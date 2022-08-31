#include <stdio.h>
#include <stdlib.h>

float sumOfRightsideMatrix(int matriz[12][12])
{
    int column = 11, x = 5;
    float sum = 0;

    while (x > 0)
    {
        for (int i = 1; i < column; i++)
        {
            sum += matriz[i][column];
        }
        column--;
        x--;
    }
    return sum;
}

int main()
{
    char sumOrAverage;
    float sum, average;
    int matriz[12][12];

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
        printf("%0.1f\n", average);
    }
    else
    {
        printf("%0.1f\n", sum);
    }
    return 0;
}