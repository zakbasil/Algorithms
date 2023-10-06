/*

Susan was writing a program to control the code flow using 
Switch case. She needs only onw of the case to be successful, 
but she gets multiple lines in her output.

*/

#include <stdio.h>
 
int main() {
  int i = 2;
  switch (i) {
    case 1: 
      printf("Case 1\n"); // --> 1
    case 2:
      printf("Case 2\n"); // --> 2
    case 3:
      printf("Case 3\n"); // --> 3
    default:
      printf("Default\n");
  }
}