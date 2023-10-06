#include<stdio.h>
int x =10;

void A(){
int x = 15;
printf("%d\t",x);
}

int main(){

    A();
    printf("%d",x++);
    return(0);
}
