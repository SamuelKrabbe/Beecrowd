#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    char track[50], lastChar = 'O';
    int process, machineCycles = 0, countForR = 0;

    while (scanf("%50s[^\n]", track) >= 1)
    {
        scanf("%d", &process);
        printf("%s\n%d", track, process);

        for (int i = 0; i < 50; i++)
        {
            if (countForR == 3)
            {
                countForR = 0;
                lastChar = 'O';
            }

            if (countForR < 3)
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
    }
    return 0;
}
