#include <iostream>
using namespace std;
int main(){
  hanshu()
}
int hanshu()
{
int a=0,b=0,c=0,d=0,e=0;
for (a=0;a<=3 ;a++)
  for(b=0;b<=8;b++)
    for(c=0;c<=36;c++)
      for(d=0;d<=80;d++)
       for(e=0;e<=365;e++)
       {
       if (50*a+20*b+10*c+5*d+e==365)
       cout<<"100CNYx"<<a<<" "<<"50CNYx"<<b<<" "<<"10CNYx"<<c<<" "<<"5CNYx"<<d<<" "<<"1CNYx"<<endl;
       }
}