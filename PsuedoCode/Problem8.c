/*

Carol was writing a program to print
day number based on week.
She is getting wrong answers. Since she is curious,
She wants to know what was she getting and how to rectify it.

*/

#include<stdio.h>
 
enum week{Mon, Tue, Wed, Thur, Fri, Sat, Sun};
 
int main()
{
  char day[10] = 'Wed';
  printf("%d", day);
  return 0;
}