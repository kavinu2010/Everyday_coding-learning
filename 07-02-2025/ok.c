/*#include<stdio.h>

int main(){
  int number = 12345;
  int num = number % 10;
  printf("%d", num);
  number /= 10;
  printf("%d",number);
  return 0;
}*/

#include <stdio.h>

int main() {
  int myAge = 43;
  int m;
  printf('enter the value');
  scanf("%d", &m);
  printf('the %d is ', m);
  
  printf("%d\n", myAge);
  printf("%p\n", &myAge);
  return 0;
}
 