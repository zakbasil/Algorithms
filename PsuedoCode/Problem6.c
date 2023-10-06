#include<stdio.h>

int main(){

    int *ptr;
    int x = 10;
    ptr = 10;

    if((void*) &x == ptr){
        printf("Hello World!\n%p\n%p",ptr,(void*) &x);
    }
    
return(0);
}