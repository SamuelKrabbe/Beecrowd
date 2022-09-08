#include <stdio.h>
#include <stdlib.h>

int main()
{
    int column;
    char operation[2];
    double vector[12][12], soma = 0.0, media;

    scanf("%d", &column);
    scanf("%s", operation);

    for (int i = 0; i < 12; i++)
    {
        for (int j = 0; j < 12; j++)
        {
            scanf("%lf", &vector[i][j]);

            if (j == column)
            {
                soma += vector[i][j];
            }
        }
    }

    if (operation[0] == 'M')
    {
        media = (soma / 12.0);
        printf("%.1lf\n", media);
    }
    else
    {
        if (operation[0] == 'S')
        {
            printf("%.1lf\n", soma);
        }
    }
    return 0;
}
