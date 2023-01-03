#include<stdio.h>

void swap(long x, short i, short j)
{

    if(((x>>i) & 1) != ((x>>j) & 1)) // Checks if ith and jth bits are same or not.
    {
        unsigned long mask = 1L << i | 1L << j; // Swap only if bits are different. Use a mask to swap.
        x ^= mask; // XOR with mask helps to swap. 
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