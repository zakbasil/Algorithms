#include <stdio.h>

void closestNumber(unsigned short x)
{
    short i = 0;

    while (++i < 16)
    {
        if (((x >> i) & 1) != ((x >> (i + 1)) & 1)) // Find bit inequality at ith and i+ist bits. 
        break;
    }

    x ^= (3UL << (i)); // Swap inequal bits
    printf("result: %hu\n\n", x);
}

int main()
{
    closestNumber(7);
    closestNumber(92);
    getchar();
    return (0);
}