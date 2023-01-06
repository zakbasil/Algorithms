#include <stdio.h>

unsigned Add(unsigned a, unsigned b)
{
    unsigned sum = 0, k = 1;
    unsigned ak = a, bk = a, temp_a = a, temp_b = b, carryin = 0, carryout = 0;

    while (temp_a || temp_b)
    {

        ak = a & k;
        bk = b & k;

        carryout = (ak & bk) | (ak & carryin) | (bk & carryin);
        sum |= (ak ^ bk ^ carryin);

        carryin = carryout << 1;

        k <<= 1;
        temp_a >>= 1;
        temp_b >>= 1;
    }

    return (sum | carryin);
}

unsigned Multiply(unsigned x, unsigned y)
{
    unsigned sum = 0;
    while (x)
    {
        if (x & 1)
        {
            sum = Add(sum, y);
        }

        x >>= 1;
        y <<= 1;
    }
    return (sum);
}

int main()
{

    printf("%u\n", Multiply(6, 7));
    printf("%u\n", Multiply(10, 10));
    printf("%u\n", Multiply(13, 9));
    printf("%u\n", Multiply(9, 15));
    printf("%u\n", Multiply(2, 2));

    getchar();
    return (0);
}