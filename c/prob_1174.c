#include <stdio.h>
#include <stdlib.h>

int main()
{
    float vector[100];

    for (int i = 0; i < 100; i++)
    {
        scanf("%f", &vector[i]);
    }

    for (int j = 0; j < 100; j++)
    {
        if (vector[j] <= 10)
        {
            printf("A[%d] = %.1f\n", j, vector[j]);
        }
    }
    return 0;
}