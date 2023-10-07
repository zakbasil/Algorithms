#include<stdio.h>
int main()
{
    for (int x = 10; x >= 0; x--) {
        int z = x & (x >> 1);
        if (z)
            printf("%d ", x);
     }
    
}