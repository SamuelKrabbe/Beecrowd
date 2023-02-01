#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <sys/time.h>
#include <time.h>

float timeDiff(struct timeval *start, struct timeval *end)
{
    return ((end->tv_sec - start->tv_sec) + 1E-6 * (end->tv_usec - start->tv_usec));
}

int main()
{
    int numerador, denominador, quociente, resto, resultado;
    double tempoDeExecucao;
    struct timeval start, end;

    gettimeofday(&start, NULL);
    scanf("%d %d", &numerador, &denominador);

    if (numerador > 0)
    {
        quociente = numerador / denominador;
        resto = numerador % denominador;
    }
    else
    {
        quociente = -1;
        resultado = quociente * denominador;

        while (resultado > numerador)
        {
            quociente--;
            resultado = quociente * denominador;
        }
        resto = numerador - resultado;
    }
    
    printf("%d %d\n", quociente, resto);

    gettimeofday(&end, NULL);
    tempoDeExecucao = timeDiff(&start, &end);
    
    printf("%.8f\n", tempoDeExecucao);

    return 0;
}
