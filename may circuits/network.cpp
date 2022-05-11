// #include <stdio.h>
// #include <iostream>
// #include <map>
// #include <vector>
// #include <time.h>
// #include <utility>
// #include <cmath>
// #include <set>
// #include <cstring>
// #include <queue>
// #include <algorithm>
// using namespace std;
 
// #define ll long long int
// #define ipair pair<int, int>
// #define tpair pair<ipair, int>
// #define mod 1000000007
// #define mod2 100000007
// #define pb push_back
// #define mp make_pair
// #define ff first
// #define ss second
// #define rep(i,n) for(i=0;i<n;i++)
// #define fu(i,a,n) for(i=a;i<=n;i++)
// #define fd(i,n,a) for(i=n;i>=a;i--)
// #define gi(n) scanf("%d",&n)
// #define gl(n) scanf("%lld",&n)
// #define pl(n) printf("%lld",n)
// #define pi(n) printf("%d",n)
// #define pp printf(" ")
// #define pn printf("\n")
// #define MAX 2000005
// #define LN 17
 
// ll fact[MAX];
// ll ifact[MAX];
// int calc(int a, int b) {
//     int ans = 1;
//     while(b) {
//         if(b&1) {
//             ans = (ans * 1LL * a)%mod;
//         }
//         a = (a * 1LL * a)%mod;
//         b>>=1;
//     }
//     return ans;
// }
 
// void init() {
//     int i, mx = 2000000;
//     fact[0] = 1;
//     fu(i, 1, mx) {
//         fact[i] = (fact[i - 1] * i)%mod;
//     }
//     ifact[mx] = calc(fact[mx], mod - 2);
//     fd(i, mx, 1) {
//         ifact[i - 1] = (ifact[i] * i)%mod;
//     }
// }
// ll getRes(ipair v1, ipair v2) {
//     if(v1.ff > v2.ff || v1.ss > v2.ss) {
//         return 0;
//     }
//     int dis1 = v2.ff - v1.ff;
//     int dis2 = v2.ss - v1.ss;
//     ll val = (ifact[dis1] * ifact[dis2])%mod;
//     return (val * fact[dis1 + dis2])%mod;
// }
// ll solve(vector<ipair> &vec, int n, int m) {
//     sort(vec.begin(), vec.end());
//     int k = vec.size();
//     if(k && vec[k - 1].ff == n && vec[k - 1].ss == m) {
//         return 0;
//     }
//     vec.pb(mp(n, m));
//     int sol[k + 1];
//     sol[0] = getRes(mp(1, 1), vec[0]);
//     int i, j;
//     fu(i, 1, k) {
//         sol[i] = getRes(mp(1, 1), vec[i]);
//         rep(j, i) {
//             ll val = (sol[j] * getRes(vec[j], vec[i]))%mod;
//             sol[i] = (sol[i] - val + mod)%mod;
//         }
//     }
//     return (ll)sol[k];
// }
// int main() {
//     init();
//     int n, m, k, w;
//     scanf("%d %d %d %d", &n, &m, &k, &w);
//     int c = 0;
//     int i, j, x, y;
//     ll v;
//     vector<ipair> v1;
//     vector<ipair> v2;
//     vector<ipair> v3;
//     rep(i, k) {
//         scanf("%d %d %lld", &x, &y, &v);
//         if(v%mod == 0) {
//             v1.pb(mp(x, y));
//             v3.pb(mp(x, y));
//         }
//         if(v%mod2 == 0) {
//             v2.pb(mp(x, y));
//             v3.pb(mp(x, y));
//         }
//     }
//     ll res = (solve(v1, n, m) + solve(v2, n, m) - solve(v3, n, m) + mod)%mod;
//     pl(res);
//     pn;
//     return 0;
// }


#include<iostream>
using namespace std;
int k,n,done=0;

struct waiting{
  int satisfy;
  int index;
  waiting *prev;
  waiting *next;
};

waiting* head=NULL;

int min(int *arr){
  int i,min=INT8_MAX,ans;

  for(i=0;i<k;i++){
    if(arr[i]<min){
        min=arr[i];
        ans=i;
    }
  }
  cout<<"min="<<min<<endl;
  return ans;
}

waiting* seek(){
  waiting* ptr;
  ptr=head;
  waiting* max_ptr;
  int max=-1;
  while(ptr != NULL){
    if(max < (ptr ->satisfy)){
      max=ptr->satisfy;
      max_ptr = ptr;
    }
    ptr=ptr->next;
  }
  return max_ptr;
}

void opp(int sat,int ind)
{
  waiting* newdata= (struct waiting*) malloc(sizeof(struct waiting));
  newdata->satisfy = sat;
  newdata->index = ind;
  newdata->next = head;
  newdata->prev = NULL;
  if(head != NULL){
    head->prev = newdata;
  }
  head=newdata;
}

void poo(int t, int *arr){
  int i, diff;
  for(i=0;i<k;i++){
    if(arr[i]==0){
      continue;
    }
    diff=arr[i]-t;
    if(diff>0){
      arr[i] = diff;
    }
    else{
      done++;
      arr[i]=0;
    }
  }
}

void drop(waiting *item){
  waiting *temp;
  if(item == head){
    head = item->next;
  }
  else{
    temp=item->prev;
    temp->next=item->next;
    temp=item->next;
    if(temp != NULL){
      temp->prev=item->prev;
    }
  }
  free(item);
}

void display(){
  waiting* ptr;
  ptr=head;
  while(ptr != NULL){
    cout<<ptr->index<<" ";
    ptr=ptr->next;
  }
  cout<<endl;
}

int main(){
  cin>>n>>k;
  int arrival[n],cook_time[n],pri[n];
  int chefs[k]={0},timec=0,lowest,low_time;
  int checked=0, i, StartsAt[n];
  waiting* hi_pri;

  for(i=0;i<n;i++){
    cin>>arrival[i];
  }

  for(i=0;i<n;i++){
    cin>>cook_time[i];
  }

  for(i=0;i<n;i++){
    cin>>pri[i];
  }

  while (done<n){
    lowest=min(chefs);
    low_time=chefs[lowest];
    cout<<"low="<<lowest<<endl;
    if(low_time>0){
      poo(low_time, chefs);
      timec+=low_time;
    }
    // cout<<"chk="<<checked<<"done="<<done<<endl;
    while(arrival[checked]<=timec && checked<n){
      opp(pri[checked],checked);
      checked++;
    }

    if(head == NULL){
      i=arrival[checked];
      poo(i-timec, chefs);
      chefs[lowest]=cook_time[checked];
      StartsAt[checked]=i;
      timec=i;
      checked++;
    }
    else{
      hi_pri=seek();
      i=hi_pri->index;
      chefs[lowest]=cook_time[i];
      StartsAt[i]=timec;
      drop(hi_pri);
    }
  }

  for(i=0;i<n;i++)
  {
    cout<<StartsAt[i]<<" ";
  }
}
