typedef long long ll;
typedef vector<int> VI;
typedef pair<int,int> PII;

#define REP(i,s,t) for(int i=(s);i<(t);i++)
#define FILL(x,v) memset(x,v,sizeof(x))

const int INF = (int)1E9;
#define MAXN 100005

class Solution {
public:
  bool isLetter(char c) {
    return ('a' <= c && c <= 'z') || ('A' <= c && c <= 'Z');
  }
  char toLowercase(char c) {
    if ('a' <= c && c <= 'z') return c;
    return (c - 'A' + 'a');
  }
  string mostCommonWord(string paragraph, vector<string>& banned) {
    set<string> bans;
    REP(i,0,banned.size()) bans.insert(banned[i]);
    map<string, int> cnt;
    int maxfreq = -1;
    REP(i,0,paragraph.size()) {
      if (!isLetter(paragraph[i])) continue;
      int j = i;
      string word = "";
      while (j < paragraph.size() && isLetter(paragraph[j])) {
        word += toLowercase(paragraph[j]);
        j++;
      }
      if (bans.find(word) == bans.end()) {
        maxfreq = max(maxfreq, ++cnt[word]);
      }
      i = j - 1;
    }
    for (auto it = cnt.begin(); it != cnt.end(); it++) {
      if (it->second == maxfreq) return it->first;
    }
  }
};