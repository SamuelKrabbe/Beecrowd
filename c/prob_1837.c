#include <stdio.h>
#include <stdlib.h>

int main()
{
    int numerador, denominador, quociente, resto, resultado;

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
    return 0;
}
