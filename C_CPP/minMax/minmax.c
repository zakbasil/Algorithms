#include<stdio.h>
#include<stdlib.h>

int* sort(int* arr){
    //logic for sort
}

int main()
{
    int arr[] = {1,4,7,2}, k = 2, n = 4;
    int i, unfairness;
    arr = sort(arr); //add logic for sort

    unfairness = arr[k] - arr[0];

    for(i=0;i<n-k+1;i++){
        if(unfairness>arr[k+i-1]-arr[i]){
            unfairness = arr[k+i-1]-arr[i];
        }
    }
    printf("%d",unfairness);
}