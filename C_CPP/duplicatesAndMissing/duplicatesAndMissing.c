#include<stdio.h>
#include<stdlib.h>
int main()
{
    int arr[10];
    int i,j,count;

    scanf("%d",&count);
    for(i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }

    for(i=0;i<n;i++){

        if(arr[abs(arr[i])-1]>0){
            arr[abs(arr[i])-1] = -arr[abs(arr[i])-1]; 
        }
        else{
            printf("%d\n",abs(arr[i]));
        }
    }

    for(i=0;i<size;i++)
    {
        if(arr[i]>0){
            printf("%d",(i+1));
        }
    }
}