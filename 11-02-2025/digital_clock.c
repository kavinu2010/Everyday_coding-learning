/* #include<stdio.h>
#include<time.h>
#include<unistd.h>
#include<stdlib.h>

int main() 
{
  int hour, minute, seconds;
  hour = minute = seconds = 0;
  while(1)
  {
    system("clear");
    printf("%02d : %02d : %02d", hour, minute, seconds);
    fflush(stdout);
    seconds++;

    if (seconds == 60)
    {
      minute += 1;
      seconds = 0;
    }
     if(minute==60)
     {
    hour += 1;
    minute = 0;
     }
  if(hour==24){
    hour = 0;
    minute = 0;
    seconds = 0;
  }
  sleep(1);
  }
  return (0);
}

#include<stdio.h>
#include<time.h>

int main(){
  time_t s, val = 1;
  struct tm* current_time;

  s = time(NULL);
  current_time = localtime(&s);

  printf("%02d : %02d : %02d", current_time->tm_hour, current_time->tm_min, current_time->tm_sec);
  return 0;
}
*/

#include<stdio.h>

int main(){
  char ch;
  char pass[20];
  int i = 0;

  ch = getchar();
  if(ch==13)
  {
    pass[i] = '\0';
     
  }
  else{
    pass[i++] = ch;
    printf("*");

  }
  printf("you entered : %s \n ", pass);
  FILE * ptr;
  ptr = fopen("password.txt", "r");

  return 0;

}
