#include <stdio.h>
#include <stdlib.h>
#include <math.h>

long long int getNumOfDigits(long long int n);

int main()
{
    int cases;

    while (scanf("%d", &cases) != EOF)
    {
        int savedChars = 0, a, b;
        long long int telNumber[2], numOfDigits;

        for (int i = 0; i < cases; i++)
        {
            scanf("%lld", telNumber[i]);
        }

        numOfDigits = getNumOfDigits(telNumber[0]);

        for (int j = 0; j < cases; j++)
        {
            while ((numOfDigits != -1) && ((j + 1) != cases))
            {
                numOfDigits--;

                a = telNumber[j] / pow(10, numOfDigits);
                b = telNumber[j + 1] / pow(10, numOfDigits);

                if (a == b)
                    savedChars++;
                else
                    break;
            }
        }
        printf("%d\n", savedChars);
    }

    return 0;
}

long long int getNumOfDigits(long long int n)
{
    long long int numOfDigits;

    while ((n % 10) != 0)
    {
        n /= 10;
        numOfDigits++;
    }
    return numOfDigits;
}