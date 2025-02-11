#include<stdio.h>
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
