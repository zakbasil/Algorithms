#include<stdio.h>
#include<string.h>

int main()
{
    char ch[30];
    int flag=0;
    short unsigned int count=0;
    
    for( i=0; ch[i]!='\0';i++) count++;
   
    for(i=0;i<count/2;i++)
    {
        if(ch[i] != ch[count - i - 1])
        {
            flag=1;
            break;
        }
    }
    if(flag==1)
        printf("String is not palindrome.\n");
    else
        printf("String is plindrome.\n");
}