#include <iostream>
using namespace std;
int main()
{
    int i,j=0,k,flag;
    int a[4]={1,3,5,7},b[4]={4,6,8,9},c[8]; 
    for(i = 0;i<4;) 
    {      
            if (a[i]<b[j])
            {
                cout<<"<"<<i<<j;
                c[i+j]=a[i];
                i++;
            }
            if (a[i]>b[j])
            {
                cout<<">"<<i<<j;
                j++;
                c[i+j]=b[j];
                i--;
            }
    }

    
for(int d=0;d<8;d++)
    cout<<endl<<c[d];
}