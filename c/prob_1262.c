#include <stdio.h>
#include <stdlib.h>
#define LENGHT 51

int main()
{
    char track[LENGHT];
    int process;
    
    while (scanf("%s", track) != EOF)
    {
        scanf("%d", &process);

        char lastChar = 'O';
        int machineCycles = 0, countForR = 0, arrayLenght = 0;


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
                if (track[i] == 'W')
                {
                    machineCycles++;
                    lastChar = track[i];
                    countForR = 0;
                }
                else
                {
                    if (track[i] == 'R' && lastChar != 'R')
                    {
                        machineCycles++;
                        lastChar = track[i];
                        countForR++;
                    }
                    else
                    {
                        lastChar = track[i];
                        countForR++;
                    }
                }
                
            }
        }
        printf("%d\n", machineCycles);
    }
    return 0;
}
