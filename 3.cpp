#include <iostream>
using namespace std;
int main()
{
    int i,j,k,flag;
    int a[8]={1,3,5,7},b[4]={4,6,8,9}; 
    for(i = 0;i<4;i++) //b
    {      
        for(j= 0;j<4;j++)
            if (b[i]<a[j])
            {
                a[j+2]=a[j+1];
                a[j+1]=a[j];
                a[j]=b[i];
                for(int d=0;d<8;d++)
                cout<<a[d];
            }
            if (b[i]>a[3])
            {
                a[6]=b[2];
                a[7]=b[3];
               
                for(int d=0;d<8;d++)
                cout<<a[d];
            }
            
    }

    

}