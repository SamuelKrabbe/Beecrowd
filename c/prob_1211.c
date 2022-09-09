#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int getNumOfDigits(long long int n);

int main()
{
    int cases;

    while (scanf("%d", &cases) != EOF)
    {
        int savedChars = 0, a, b, numOfDigits;
        long long int telNumber[cases];

        for (int i = 0; i < cases; i++)
        {
            scanf("%lld", &telNumber[i]);
        }

        for (int j = 0; j < cases; j++)
        {
            numOfDigits = getNumOfDigits(telNumber[0]);

            while ((numOfDigits >= 0) && ((j + 1) < cases))
            {
                // printf("%lld", numOfDigits);
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

int getNumOfDigits(long long int telNumber)
{
    int numOfDigits = 1;

    while (telNumber <= 10)
    {
        telNumber /= 10;
        numOfDigits++;
    }
    return numOfDigits;
}