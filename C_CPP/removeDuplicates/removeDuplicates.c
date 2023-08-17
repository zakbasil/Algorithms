#include<stdio.h>
#include<stdlib.h>

int main()
{

int arr[20],temp[20];
int i,j=0;

scanf("%d",&count);
for(i=0;i<count;i++){
    scanf("%d",&arr[i]);
}
i=0;
while(i<count-1){
    if(arr[i] != arr[i+1]){
        temp[j++] = arr[i]
    }
    i++;
}

temp[j++] = arr[count-1]

for(i=0;i<j;i++){
    print("%d",temp[i]);
}

    return(0);
}