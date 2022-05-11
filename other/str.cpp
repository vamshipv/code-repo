#include<iostream>
using namespace std;

int main()
{
  int test;
  cin>>test;
  while(test--)
  {
    int n;
    cin>>n;
    int count_a=0,count_b=0,min_swap=0,tot=0,i,b_before=0,a_after=0,swaps[n];
    char strng[n];
    cin>>strng;
    for(i=0;i<n;i++)
    {
      if(strng[i]=='A')
      {
        count_a++;
      }
    }
    count_b=n-count_a;
    a_after=count_a;
    min_swap=n;

    for(i=0;i<n;i++)
    {
      if(strng[i]=='A')
      {
        a_after--;
      }
      else
      {
        b_before++;
      }
      tot=a_after+b_before;
      swaps[i]=tot;
    }

    min_swap=count_a;
    for(i=0;i<n;i++)
    {
      if(min_swap>swaps[i])
      {
        min_swap=swaps[i];
      }
    }

  cout<<min_swap<<endl;
  }
}
