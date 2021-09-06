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

vector<string> gen(string &s,int l,int r){
	string t="";
	vector<string>ans;
	if(s[l]!='0'){
		t="";
		rep(i,l,r+1)t+=s[i];
		ans.pb(t);
		if(s[r]!='0')
		rep(i,l,r){
			t="";
			rep(j,l,i+1)t+=s[j];
			t+=".";
			rep(j,i+1,r+1)t+=s[j];
			ans.pb(t);
		}
	}
	else if(l==r){
		t="0";
		ans.pb(t);
	}
	else if(s[r]!='0'){
		t="0.";
		rep(i,l+1,r+1)t+=s[i];
		ans.pb(t);
	}
	return ans;
}
class Solution {
public:
    vector<string> ambiguousCoordinates(string s) {
		s=s.substr(1,SZ(s)-2);        
		int n=SZ(s);
		vector<string>ans,L,R;
		rep(i,0,n-1){
			L=gen(s,0,i);
			if(L.empty())continue;
			R=gen(s,i+1,n-1);
			if(R.empty())continue;
			for(auto &x:L){
				for(auto &y:R){
					string t="("+x+", "+y+")";
					ans.pb(t);
				}
			}
		}
		sort(all(ans));
		ans.erase(unique(all(ans)),ans.end());
		return ans;
	}
};

