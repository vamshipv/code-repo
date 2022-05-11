#include<iostream> 
using namespace std;
int main()
{
	long long int p ,h, n;
	cin>>n;
	for (int i=0;i<n;i++){
		cin>>h>>p;
		if (p >= h/2){
			cout<<1<<"\n";
		}
		else
			cout<<0<<"\n";
	}
return 0;
}
