/*

Integer x, y
Set x = 10, y = 6
do{
  Print x 
  x = x + y++ - 8
}
while(x <= 10)
end do while

*/

#include<stdio.h>

int main(){

    int x = 10;
    int y = 6;
    do{
    printf("%d\n",x);
    x = x + y++ - 8;
    } while(x <= 10);
    return(0);
}