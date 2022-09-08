#include <stdio.h>
#include <stdlib.h>

float lowerLeftDiagonalSum(double vector[12][12]);

int main()
{
    char operation[2];
    double vector[12][12];
    float sum = 0.0, media;

    scanf("%s", operation);

    for (int i = 0; i < 12; i++)
    {
        for (int j = 0; j < 12; j++)
        {
            scanf("%lf", &vector[i][j]);
        }
    }

    sum = lowerLeftDiagonalSum(vector);

    if (operation[0] == 'M')
    {
        media = (sum / 66.0);
        printf("%.1lf\n", media);
    }
    else
    {
        if (operation[0] == 'S')
        {
            printf("%.1lf\n", sum);
        }
    }
    return 0;
}

float lowerLeftDiagonalSum(double vector[12][12])
{
    float sum = 0.0;
    
    for (int row = 11; row > 0; row--)
    {
        for (int column = (row - 1); column >= 0; column--)
        {
            sum += vector[row][column];
        }
    }
    return sum;
}
