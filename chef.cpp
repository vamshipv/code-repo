#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int32_t main()
{
    int testcase;
    cin >> testcase;
    while (testcase --)
    {
        int D,d,P,Q;
        cin>> D>> d >> P >> Q;
        int days = D/d;
        int reamning = D%d;
        int prod = 0;
        int heist = 0;
        int temp = days - 1;
        heist = (days * P) + ((((temp)*(temp + 1))/2)*Q);
        heist = heist * d;
 
        if ( reamning >= 1)
        {
            heist = heist + ((P + ((days) * Q))*reamning);
        }
        cout << heist << "\n";
    }
 
    return 0;
}