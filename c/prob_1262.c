#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    char *track = (char *)calloc(50, sizeof(char)), lastChar = 'O';
    int process, machineCycles = 0, countForR = 0;

    while (scanf("%50s", track) != EOF)
    {
        scanf("%d", &process);

        for (int i = 0; i < 50; i++)
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
    }
    return 0;
}
