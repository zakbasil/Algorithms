/*

Nixon is an lab exam and has a problem statement to display 
the size of a pointer. He got a zero out o 10 marks. 
Point out his error.

*/

#include<stdio.h>

int main(){

    int x = 10;
    int *ptr = &x;

    printf("%d",sizeof(ptr));

}