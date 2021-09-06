#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <algorithm>
#include <numeric>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <cmath>
#include <cstring>
#include <unordered_set>
#include <unordered_map>
using namespace std;

#define pb push_back
#define fst first
#define snd second

typedef long long ll;
typedef pair<int,int> pii;
template<typename T> using min_queue=priority_queue<T,vector<T>,greater<T> >;

const ll MOD=1e9+7;

class Solution {
public:
    string mostCommonWord(string par, vector<string>& bd) {
      istringstream ss(par);
      map<string,int> freq;
      set<string> bad;
      for(auto& s:bd) bad.insert(s);
      string s;
      while(ss>>s){
	string tmp;
	for(char c:s) if(isalpha(c)) tmp+=tolower(c);
	if(bad.count(tmp)) continue;
	freq[tmp]++;
      }
      int best=0;
      string res;
      for(auto& pr:freq){
	if(pr.snd>best) best=pr.snd,res=pr.fst;
      }
      return res;
    }
};

