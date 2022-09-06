#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define LENGHT 51

int main(void)
{
    char track[LENGHT], lastChar = 'O';
    int process, machineCycles = 0, countForR = 0, arrayLenght = 0;

    while (scanf("%50s", track) != EOF)
    {
        scanf("%d", &process);

        while (track[arrayLenght] != '\0')
        {
            arrayLenght++;
        }

        for (int i = 0; i < arrayLenght; i++)
        {
            if (countForR == process)
            {
                countForR = 0;
                lastChar = 'O';
            }

            if (countForR < process)
            {
                if (lastChar = 'R')
                {
                    if (track[i] == 'W')
                    {
                        machineCycles++;
                        lastChar = track[i];
                        countForR = 0;
                    }
                    else
                    {
                        if (track[i] == 'R')
                        {
                            lastChar = track[i];
                            countForR++;
                        }
                    }
                }
                else
                {
                    if (track[i] == 'W')
                    {
                        machineCycles++;
                        lastChar = track[i];
                        countForR = 0;
                    }
                    else
                    {
                        if (track[i] == 'R')
                        {
                            machineCycles++;
                            lastChar = track[i];
                            countForR++;
                        }
                    }
                }
            }
        }
        printf("%d\n", machineCycles);

        machineCycles = 0;
        countForR = 0;
        lastChar = 'O';
        arrayLenght = 0;
    }
    return 0;
}
