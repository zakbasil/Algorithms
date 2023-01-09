#include <stdio.h>

void divide(unsigned x, unsigned y)
{
    unsigned result = 0;
    int power = 32;
    unsigned long long y_power = (unsigned long long)y << power;

    while (x >= y)
    {
        while (y_power > x)
        {
            y_power >>= 1;
            --power;
        }
        result += 1U << power;
        x -= y_power;
    }

    printf("%u", result);
}

int main()
{
    divide(4,2);
    divide(20,5);
    getchar();
    return (0);
}