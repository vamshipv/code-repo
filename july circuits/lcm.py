# # import math
# # t = int(input())
# # n,m,k = map(int,input().split())
# # lst = list(map(int,input().split()))
# # for i in range(len(lst)):
# #     lst[i] = (lst[i]**k)%m
# # def lcmfinal(num1,num2):
# #     if num1>num2:
# #         num = num1
# #         den = num2
# #     else:
# #         num = num2
# #         den = num1
# #     rem = num % den
# #     while rem!=0:
# #         num = den
# #         den = rem
# #         rem =num % den
# #     gcd = den
# #     lcm = int(int(num1*num2)/int(gcd))
# #     return lcm
# # num1 = lst[0]
# # num2 = lst[1]
# # lcm = lcmfinal(num1,num2)
# # for i in range(2,n):
# #     lcm = lcmfinal(lcm,lst[i])
# # print(lcm%m)
# import math
# t = int(input())
# for i in range(t):
#     n,m,k = map(int,input().split())
#     lst = list(map(int,input().split()))

# #lcm code from geeksforgeeks
#     # def lcmfinal(num1,num2):
#     #     if num1>num2:
#     #         num = num1
#     #         den = num2
#     #     else:
#     #         num = num2
#     #         den = num1
#     #     rem = num % den
#     #     while rem!=0:
#     #         num = den
#     #         den = rem
#     #         rem =num % den
#     #     gcd = den
#     #     lcm = int(int(num1*num2)/int(gcd))
#     #     return lcm

#     def lcmfinal(num1,num2):
#         gcd = math.gcd(num1,num2)
#         result = (num1*num2)/gcd
#         return int(result)
#     num1 = lst[0]
#     num2 = lst[1]
#     lcm = lcmfinal(num1,num2)
#     for i in range(2,n):
#         lcm = lcmfinal(lcm,lst[i])
# # print(lcm)
#     ans=(lcm**k)%m
#     print(ans)


#include <bits/stdc++.h>
using namespace std;
#define int long long int
int tree1[300002];
int tree2[300002];
vector<pair<int, int>> lst;
int n, i, a, b, op, y;

void merge(int op, int y) {
    int x1 = find(op);
    int y1 = find(y);

    if (tree1[x1] > tree1[y1]) {
        tree2[y] = op;
        tree1[x1] += tree1[y1];
    } else {
        tree2[op] = y;
        tree1[y1] += tree1[x1];
    }
}

int find(int op) {
    if (op != tree2[op]) {
        tree2[op] = find(tree2[op]);
    }
    return tree2[op];
}

bool same(int op, int y) 
{ 
    return find(op) == find(y); 
}


int main() {

    cin >> n;
    vector<int> ans(n + 1);

    for (i = 1; i <= n; i++) {
        tree2[i] = i;
        tree1[i] = 1;
    }

    for (i = 1; i <= n - 1; i++) {
        cin >> a >> b;
        lst.push_back(make_pair(a, b));
    }

    int c[n + 1];
    for (i = 1; i <= n; i++) {
        cin >> c[i];
    }

    ans[n] = (n * (n - 1)) / 2;

    for (i = n - 1; i >= 0; i--) {
        op = lst[i].first;
        y = lst[i].second;

        if (same(op, y)) {
            ans[i] = ans[i + 1];
            continue;
        }

        int s1 = tree1[find(op)];
        int s2 = tree1[find(y)];
        merge(op, y);

        ans[i] = max(ans[i + 1] - (s1 * s2), 0LL);
    }
    int z;

    for (i = 1; i <= n - 1; i++) {
        cin >> z;
        cout << ans[z] << '\n';
    }
}


#include <bits/stdc++.h>

using namespace std;
#define ll long long int
int par[300002];
int sz[300002];
vector<pair<ll, ll>> arr;
ll n, i, a, b, x, y;

ll find(ll x) {
    if (x != par[x]) {
        par[x] = find(par[x]);
    }
    return par[x];
}

bool same(ll x, ll y) { return find(x) == find(y); }

void merge(ll x, ll y) {
    ll x1 = find(x);
    ll y1 = find(y);

    if (sz[x1] > sz[y1]) {
        par[y] = x;
        sz[x1] += sz[y1];
    } else {
        par[x] = y;
        sz[y1] += sz[x1];
    }
}

int main() {

    cin >> n;
    vector<ll> ans(n + 1);

    for (i = 1; i <= n; i++) {
        par[i] = i;
        sz[i] = 1;
    }

    for (i = 1; i <= n - 1; i++) {
        cin >> a >> b;
        arr.push_back(make_pair(a, b));
    }

    int c[n + 1];
    for (i = 1; i <= n; i++) {
        cin >> c[i];
    }

    ans[n] = (n * (n - 1)) / 2;

    for (i = n - 1; i >= 0; i--) {
        x = arr[i].first;
        y = arr[i].second;

        if (same(x, y)) {
            ans[i] = ans[i + 1];
            continue;
        }

        ll s1 = sz[find(x)];
        ll s2 = sz[find(y)];
        merge(x, y);

        ans[i] = max(ans[i + 1] - (s1 * s2), 0LL);
    }
    int z;

    for (i = 1; i <= n - 1; i++) {
        cin >> z;
        cout << ans[z] << '\n';
    }
}