#include<stdio.h>
int main(){

    int x = 5;
    int c = x++;
    int b = ++x;


    printf("%d %d %d",x,c,b);
    return(0);
}