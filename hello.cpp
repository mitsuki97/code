
#include<iostream>
using namespace std;
int main()
{
	int val[7] = { 0,1,2,5,10,20,50 };
	int f[101][7];
	memset(f, 0, sizeof(f));
 
	for (int j = 0; j <= 6; j++)
		f[0][j] = 1;
	
	for (int j = 1; j <= 6; j++)
	{
		for (int i = 1; i <= 100; i++)
		{
			if (i - val[j] < 0)
				f[i][j] = f[i][j - 1];
			else
				f[i][j] = f[i - val[j]][j] + f[i][j - 1];
		}
	}
 
 
	//cout << test(0, 100) << endl;
	//cout << ans << endl;
	cout << f[100][6] << endl;