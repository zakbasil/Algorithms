#include<stdio.h>
#include<string.h>
#include<math.h>

int main()
{
    int flag=0, input;
    int numDigits;
    scanf("%d",&input);
    numDigits = log10(input) + 1;
    int mask = pow(10,numDigits - 1)
    for(i=0;i<numDigits/2;i++)
    {
       if(input%10 != int(input/mask)){
        flag = 1;
        break;
       }

       input %= mask;
       input /= 10;
       mask /= 100;

    }
    if(flag==1)
        printf("String is not palindrome.\n");
    else
        printf("String is plindrome.\n");
}