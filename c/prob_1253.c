#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX 51

void getDecryptedText(char encryptedText[], char decryptedText[], int decoder, int encryptedTextLenght);

int main()
{
    int cases, decoder;
    char encryptedText[MAX], decryptedText[MAX];

    scanf("%d", &cases);

    for (int i = 0; i < cases; i++)
    {
        int encryptedTextLenght = 0;

        scanf("%s", encryptedText);
        scanf("%d", &decoder);

        while (encryptedText[encryptedTextLenght] != '\0')
            encryptedTextLenght++;

        getDecryptedText(encryptedText, decryptedText, decoder, encryptedTextLenght);

        for (int i = 0; i < encryptedTextLenght; i++)
        {
            if (i == (encryptedTextLenght - 1))
                printf("%c\n", decryptedText[i]);
            else
                printf("%c", decryptedText[i]);
        }
    }
    return 0;
}

void getDecryptedText(char encryptedText[], char decryptedText[], int decoder, int encryptedTextLenght)
{
    int decryptedAscii;

    for (int i = 0; i <= encryptedTextLenght; i++)
    {
        if (i == encryptedTextLenght)
        {
            decryptedText[i] = '\0';
            break;
        }

        decryptedAscii = encryptedText[i];

        if ((decryptedAscii - decoder) < 65)
            decryptedText[i] = (decryptedAscii + 26) - decoder;
        else
            decryptedText[i] = decryptedAscii - decoder;
    }
}