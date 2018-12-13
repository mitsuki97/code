#include <iostream>
using namespace std;
int main()
{
    int i,j,k,t=0;
    int a[9]={1,2,3,4};
    int b[4]={1,3,8,9};
    for(i=0;i<4;)
    {
        loop:
        i++;
        for(j=0;j<4;j++)
        {
            if(a[j]<=b[i])
            {
                for(k=(i+3);k>=i;k--)
                {
                    a[j+1]=a[j];
                    a[j]=b[i];
                    t=1;
                    cout<<"aj"a[j]<<endl;
                    break;
                }
            }   
                   
            if(t==1)
            break;
        }
    
    }
    for(i=0;i<8;i++)
    {
        cout<<a[i]<<endl;
    }
    
}
