#include <stdio.h>
#include <stdlib.h>

long long int getFactorial(int n);

int main()
{
    int x, y;
    long long int FactorialOfX, FactorialOfY, sumOfFactorials;

    while (scanf("%d %d", &x, &y) != EOF)
    {
        FactorialOfX = getFactorial(x);
        FactorialOfY = getFactorial(y);

        sumOfFactorials = FactorialOfX + FactorialOfY;

        printf("%lld\n", sumOfFactorials);
    }
    return 0;
}

long long int getFactorial(int n)
{
    if (n == 0)
        return 1;
    else
    {
        if (n == 1)
            return 1;
        else
        {
            if (n == 2)
                return 2;
            else
                return n * getFactorial(n - 1);
        }
    }
}