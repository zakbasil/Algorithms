#include<stdio.h>
#include<stdlib.h>

int main()
{
    int arr[10] ={'{','{','}','}','\0'};
    int i, count = 0, flag = 0;
    int length = 4;

    for(i=0;i<length;i++){
        if(arr[i]=='{'){
            count++;
        }
        else if(arr[i]=='}'){
            count--;
        }
        else{
            printf("Invalid character");
            break;
        }
        if(count<0){
            printf("Not matching");
            flag = 1;
            break;
        }
    }
    if(flag == 0 && count == 0){
        printf("Matching");
    }
}