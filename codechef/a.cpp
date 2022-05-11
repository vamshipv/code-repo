#include<bits/stdc++.h>
using namespace std;
int main()
{
  int po;
  cin>>po;
  while(po--)
  {
    int i,n,op;
    cin>>n;
    vector<int> v1,v2;
    for(int i=0;i<n;i++)
    {
      cin>>op;
      v1.push_back(op);
    }
    for(int i=0;i<n;i++)
    {
      cin>>op;
      v2.push_back(op);
    }
    int su1=0,su2=0,aw=0;
    for(int i=0;i<v1.size();++i)
    {
      su1+=v1[i];
      su2+=v2[i];
      if(v1[i]==v2[i] && su2==su1)
      {
        aw+=v1[i];
      }
    }
    cout<<aw<<endl;
  }
  return 0;
}