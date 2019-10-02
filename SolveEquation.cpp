//cerner_2^5_2019
/* k=1,2,3,4,...,10 is given.Let x_{i} be a positive integer and x_{i}=100.
   Find all the solutions for each of the following equations: x1³+x2³+x3³=kx1x2x3 */    
#include <iostream>
using namespace std;
int main()
{
   int count=0;
   for(int k=1;k<=10;k++)
   {
	for(int x1=1;x1<=100;x1++)
       {
		for(int x2=1;x2<=100;x2++)
           	{
			for(int x3=1;x3<=100;x3++)
                	{
                   		if(((x1*x1*x1)+(x2*x2*x2)+(x3*x3*x3)-(k*x1*x2*x3))==0)
                   		{
                        		cout<<"\n k="<<k<<",x1="<<x1<<",x2="<<x2<<",x3="<<x3;
                        		count++;
                   }
                }
           }
       }
   }
   cout<<"\nCount="<<count;
   return 0;
}