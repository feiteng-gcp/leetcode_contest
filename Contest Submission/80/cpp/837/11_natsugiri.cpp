#include<map>
#include<stdio.h>
#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<string.h>
using namespace std;

typedef long long LL;
typedef vector<int> VI;

#define REP(i,n) for(int i=0, i##_len=(n); i<i##_len; ++i)
#define EACH(i,c) for(__typeof((c).begin()) i=(c).begin(),i##_end=(c).end();i!=i##_end;++i)
#define eprintf(...) fprintf(stderr, __VA_ARGS__)

template<class T> inline void amin(T &x, const T &y) { if (y<x) x=y; }
template<class T> inline void amax(T &x, const T &y) { if (x<y) x=y; }
template<class Iter> void rprintf(const char *fmt, Iter begin, Iter end) {
    for (bool sp=0; begin!=end; ++begin) { if (sp) putchar(' '); else sp = true; printf(fmt, *begin); }
    putchar('\n');
}

vector<string> split(const string&s, char c=' ') {
    int p=0;
    vector<string>ret;
    for (int i=0; i<int(s.size()); i++) {
	if (s[i]==c) {
	    ret.push_back(s.substr(p, i-p));
	    p=i+1;
	}
    }
    ret.push_back(s.substr(p));
    return ret;
}
class Solution {
public:
    string mostCommonWord(string paragraph, vector<string>& banned) {
	vector<string> vs = split(paragraph);
	map<string, int> mp;
	EACH (e, vs) {
	    while (!e->empty() && !isalpha(e->back())) e->pop_back();
	    REP (i, e->size()) (*e)[i] = tolower((*e)[i]);
	    mp[*e]++;
	}
	EACH (e, banned) mp.erase(*e);

	int cnt = -1;
	string ret = "";
	EACH (e, mp) if (e->second > cnt) {
	    ret = e->first;
	    cnt = e->second;
	}

	return ret;
    }
};

