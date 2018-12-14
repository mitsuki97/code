#include <iostream>
using namespace std;
int main()
{int i,j,k;
int a[9]={1,2,3,4};
int b[4]={1,3,8,9};
for(i=0;i<4;i++)
for(j=0;j<4;j++)
if(a[j]<=b[i])
{for(k=(3+i);k>=i;k--)
a[j+1]=a[j];
a[j]=b[i];
continue;
}
for(i=0;i<8;i++)
cout<<a[i]<<"";
cout<<endl;
}