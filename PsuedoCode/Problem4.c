//Debug the issue in my code. I want to see an adress in the output

#include<stdio.h>

int main(){

    int *ptr;
    int x = 10;
    ptr = &x;

    if((void*) &x == ptr){
        printf("Hello World!\n");
    }

}