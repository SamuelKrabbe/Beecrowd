#include <stdio.h>
#include <stdlib.h>

unsigned long long int getFibonacciNum(int fibTerm);

int main()
{
    int cases, fibTerm;
    unsigned long long int fibonacciNum;

    scanf("%d", &cases);

    for (int i = 0; i < cases; i++)
    {
        scanf("%d", &fibTerm);

        fibonacciNum = getFibonacciNum(fibTerm);

        printf("Fib(%d) = %u\n", fibTerm, fibonacciNum);
    }

    return 0;
}

unsigned long long int getFibonacciNum(int fibTerm)
{
    long long int a = 0, b = 1;
    unsigned long long int fib;

    if (fibTerm == 0 || fibTerm == 1)
        return fibTerm;
    else
    {
        for (int i = 2; i <= fibTerm; i++)
        {
            fib = a + b;
            a = b;
            b = fib;
            printf("%d\n", fib);
        }
        printf("%d\n", fib);
        return fib;
    }
}
