#include <bits/stdc++.h>
using namespace std;

int main()
{
  int testcase;
  cin >> testcase;
  while (testcase--)
  {
    priority_queue<unsigned int> lst;
    unsigned int N, A, sum = 0, count = 0;
    long Z;
    cin >> N >> Z;
    for (int i = 0; i < N; i++)
    {
      cin >> A;
      sum += A;
      lst.push(A);
    }

    if (Z >= sum * 2)
    {
      cout << "Evacuate" << endl;
    }
    else
    {
      while (lst.top() > 0 && Z > 0)
      {
        A = lst.top();
        Z -= A;
        lst.pop();
        lst.push(floor(A / 2));
        count++;
      }
      if (Z > 0)
        cout << "Evacuate" << endl;
      else
      {
        cout << count << endl;
      }
    }
  }
}
