#include <bits/stdc++.h>
using namespace std;
#define int long long int
#define int64 unsigned long long int
signed main()
{
    int test_cases;
    cin >> test_cases;
    while (test_cases--)
    {
        int num;
        cin >> num;
        char board[8][8];
        board[0][0] = 'O';
        num--;
        for (int i = 0; i < 8; i++)
        {
            for (int j = 0; j < 8; j++)
            {
                if (i == 0 && j == 0)
                {
                    continue;
                }
                else if (num > 0)
                {
                    board[i][j] = '.';
                    num--;
                }
                else
                {
                    board[i][j] = 'X';
                }
            }
        }
        for (int i = 0; i < 8; i++)
        {
            for (int j = 0; j < 8; j++)
            {
                cout << board[i][j];
            }
            cout << endl;
        }
    }
    return 0;
}