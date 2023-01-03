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
    getchar();
    return(0);
}