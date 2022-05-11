#include<bits/stdc++.h>
using namespace std;

long long getsmallestdivnum(long long n);

int main() {
	int t
	cin>>t;
	while(t--){
		int n;
		cin>>n;
		cout<<getsmallestdivnum(n)<<endl;
	}
	return 0;
}

long long getsmallestdivnum(long long n)
{
	long long ans = 1;
	for(long long i =1; i<=n; i++)
		ans = (ans*i)/(__gcd(ans,i));
		return ans
}
