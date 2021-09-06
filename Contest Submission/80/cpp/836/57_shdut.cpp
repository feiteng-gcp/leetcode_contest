#include <bits/stdc++.h>
#include <stdlib.h>
using namespace std;
#define vi vector<int>
#define pii pair<int,int>
#define x first
#define y second
#define all(x) x.begin(),x.end()
#define pb push_back
#define mp make_pair
#define SZ(x) x.size()
#define rep(i,a,b) for(int i=a;i<b;i++)
#define per(i,a,b) for(int i=b-1;i>=a;i--)
#define pi acos(-1)
#define mod 1000000007
#define inf 1000000007
#define ll long long
#define DBG(x) cerr<<(#x)<<"="<<x<<"\n";
#define N 500010

template <class U,class T> void Max(U &x, T y){if(x<y)x=y;}
template <class U,class T> void Min(U &x, T y){if(x>y)x=y;}
template <class T> void add(int &a,T b){a=(a+b)%mod;}

int pow(int a,int b){
	int ans=1;
	while(b){
		if(b&1)ans=1LL*ans*a%mod;
		a=1LL*a*a%mod;b>>=1;
	}
	return ans;
}

const int M=20000;
struct node{
	int w,x,y,k;
	bool operator <(const node&a)const{
		return w>a.w;	
	}
};
int dp[M<<1][20][2];
class Solution {
public:
    int racecar(int t) {
		priority_queue<node>q;
		t+=M;
		q.push({0,M,0,1});
		memset(dp,63,sizeof(dp));
		dp[M][0][1]=0;
		while(!q.empty()){
			node e=q.top();
			q.pop();
			int x=e.x,v=e.y,k=e.k;
			if(dp[x][v][k]!=e.w)continue;
			if(x==t)return e.w;
			ll y=x+(1LL<<v)*(k==1?1:-1);
			if(y>=0&&y<2*M&&dp[y][v+1][k]>e.w+1){
				dp[y][v+1][k]=e.w+1;
				q.push({e.w+1,y,v+1,k});
			}
			if(dp[x][0][k^1]>e.w+1){
				dp[x][0][k^1]=e.w+1;
				q.push({e.w+1,x,0,k^1});
			}	
		}
		return -1;
	}
};


