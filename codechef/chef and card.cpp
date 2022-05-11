#include <bits/stdc++.h>
using namespace std;
#define int long long int
signed main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, morty = 0, chef = 0;
        cin >> n;
        while (n--)
        {
            int a, b, chefW = 0, mortyW = 0;
            cin >> a >> b;

            while (a > 0)
            {
                chefW += (a % 10);
                a /= 10;
            }
            while (b > 0)
            {
                mortyW += (b % 10);
                b /= 10;
            }
            if (mortyW == chefW)
            {
                morty++;
                chef++;
            }
            else
            {
                if (mortyW > chefW)
                {
                    morty++;
                }
                else
                {
                    chef++;
                }
            }
        }
        if (chef == morty)
        {
            cout << 2 << " " << chef << endl;
        }
        else
        {
            if (chef > morty)
            {
                cout << 0 << " " << chef << endl;
            }
            else
            {
                cout << 1 << " " << morty << endl;
            }
        }
    }
    return 0;
}