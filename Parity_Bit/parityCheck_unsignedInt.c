#include <stdio.h>

void checkParity(unsigned int x)
{

    short result = 0;
    while (x)
    {
        result ^= 1;
        x &= (x - 1);
    }
    printf("%u\n", result);
}

int main()
{
    checkParity(5);   // 5   -> 0000101 Result => 0 -> Even Parity
    checkParity(7);   // 6   -> 0000111 Result => 1 -> Odd Parity
    checkParity(10);  // 10  -> 0001010 Result => 0 -> Even Parity
    checkParity(100); // 100 -> 1100100 Result => 1 -> Odd Parity
    getchar();
    return 0;
}