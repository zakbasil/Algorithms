#include<stdio.h>

void swap(long x, short i, short j)
{
    if(((x>>i) & 1) != ((x>>j) & 1))
    {
        unsigned long mask = 1L << i | 1L << j;
        x ^= mask;
    }
    printf("%ld", x);

}

int main()
{
    swap(10,3,2); // 1010 changes to 0110. Output is 6
    swap(11,3,2); // 7
    swap(32,4,5); // 16
    getchar();
    return(0);
}