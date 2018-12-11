#include <stdio.h>
#include<iostream.h>
main()
{
int a=b=c=d=e=0;
for (a=0;a<=2;a++)
  for(b=0;b<=5;b++)
    for(c=0;c<=10;c++)
      for(d=0;d<=20;d++)
       for(e=0;e<=100;e++)
       {
       if (50*a+20*b+10*c+5*d+e==100)
     printf("50,20,10,5,1分别有：%d，%d，%d，%d，%d\n",a,b,c,d,e);
       }
}
