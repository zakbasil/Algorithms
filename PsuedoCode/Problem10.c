/*

Integer value, n 
Set value = 32, n = 1 
while(value greater than equal to n) 
  value = value >> 1 
end loop 
Print value

*/
#include<stdio.h>

int main(){

    int x =10;
    while(x)
    x >>=1;
    printf("%d",x);
    return(0);
}
