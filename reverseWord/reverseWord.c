#include <stdio.h>

void rev(short x)
{
    const short KeyLength = 4;
    const short bitmask = 0x0f;                                // 00000000 00000111
    const short precomputedCache[] = {0x00, 0x08, 0x04, 0x0c, 0x02, 0x0a, 0x06, 0x0e, 0x01, 0x09, 0x05, 0x0d, 0x03, 0x0b, 0x07, 0x0f}; // 0000 1000 0100 1100 0010 1010 0110 1110 0001 1001 0101 1101 0011 1011 0111 1111
    short result = precomputedCache[(x & bitmask)] << 3 * KeyLength |
                   precomputedCache[(x >> KeyLength) & bitmask] << 2 * KeyLength |
                   precomputedCache[(x >> (2 * KeyLength)) & bitmask] << KeyLength |
                   precomputedCache[(x >> (3 * KeyLength)) & bitmask];

    printf("%hu\n", result);
}

int main()
{
    rev(1); // output 32768
    rev(0); // output 0
    rev(10); // output 20480
    getchar();
    return (0);
}