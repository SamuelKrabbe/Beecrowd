#include <stdio.h>
#include <stdlib.h>

long long int getFibonacciNum(fibTerm);

int main()
{
    int cases, fibTerm;
    long long int fibonacciNum;

    scanf("%d", &cases);

    for (int i = 0; i < cases; i++)
    {
        scanf("%d", &fibTerm);

        fibonacciNum = getFibonacciNum(fibTerm);

        printf("Fib(%d) = %d\n", fibTerm, fibonacciNum);
    }

    return 0;
}

long long int getFibonacciNum(fibTerm)
{
    int a = 0, b = 1;
    long long fib;

    if (fibTerm <= 0)
        return 0;
    else
    {
        if (fibTerm == 1)
            return 1;
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
}