#include <stdio.h>
#include <stdlib.h>

int getFibonacciNum(int fibTerm);

int main()
{
    int cases, fibTerm;
    int fibonacciNum;

    scanf("%d", &cases);

    for (int i = 0; i < cases; i++)
    {
        scanf("%d", &fibTerm);

        fibonacciNum = getFibonacciNum(fibTerm);

        printf("Fib(%d) = %d\n", fibTerm, fibonacciNum);
    }

    return 0;
}

int getFibonacciNum(int fibTerm)
{
    int a = 0, b = 1;
    int fib;

    if (fibTerm == 0 || fibTerm == 1)
        return fibTerm;
    else
    {
        for (int i = 2; i <= fibTerm; i++)
        {
            fib = a + b;
            a = b;
            b = fib;
        }
        return fib;
    }
}
