#include <iostream>
using namespace std;
int main()
{
    int g,i,j,k,flag;
    int m=4,n=4;
    int b[4]={2,3,4,8},a[8]={1,2,3,4};
 
    //m和n应该对应着数组a和数组b的个数 
   //i是数组b遍历时候下标 j是数据a遍历时候下表
    for(i = 0;i < n; i++)    
    {
        flag = 1;
       
        //数组b遍历
        for(j = 0; j < m; j++)  
        {
            //数组a遍历
            //如果b中遍历的值比a遍历的小 
            if(b[i] < a[j])
           {
                for(k = m+i; k > j; k--)
                {
                    a[k] = a[k - 1];//按照倒序赋值腾出一个a数组空位放置b数组遍历的值
                }
                a[j] = b[i];//把b数组中该值插入a数组对应位置
                flag = 0;//改变flag的值
            
            }
            if(flag==0) break;
            else a[m] = b[i];//如果flag值没改变 表示比b该值比a数组所有的值都大 直接插入
        }
        
        
        m++;//a位置增加1
    }

    for(int d=0;d<8;d++)
    cout<<a[d]<<endl;
}