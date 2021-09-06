#define PB                  push_back
#define F                   first
#define S                   second

#define REP(i,from,to)      for(auto i=(from); i<=(to); ++i)
#define PER(i,from,to)      for(auto i=(from); i>=(to); --i)
#define REP_IF(i,from,to,assert)   for(auto i=(from); i<=(to); ++i) if (assert)

#define FOR(i,less_than)    for (auto i=0; i<(less_than); ++i)
#define FORI(i, container)  for (auto i=0; i<(container).size(); ++i)
#define FORI_IF(i, container, assert) for (auto i=0; i<(container).size(); ++i) if (assert)
#define ROFI(i, container)  for (auto i=(container).size()-1; i>=0; --i)

#define FOREACH(elem, container)  for (auto elem : (container))
#define FILL(container, value)    memset(container, value, sizeof(container))
#define ALL(container)            (container).begin(), (container).end()
#define SZ(container)             (int)((container).size())

#define BACK(set_map)       *prev((set_map).end(), 1)
#define FRONT(set_map)      *(set_map).begin()

using PII = pair<int,int>;
using LL  = long long;
using VI  = vector<int>;
using VLL = vector<LL>;
using VVI = vector<VI>;
class Solution {
public:

    string mostCommonWord(string paragraph, vector<string>& banned) {
        istringstream in(paragraph);
        unordered_set<string> ban(ALL(banned));
        unordered_map<string, int> cnt;
        string w;
        while (getline(in, w, ' ')) {
            FOREACH(&c, w) c = tolower(c);
            while (w.size()>0 && !isalpha(w[0])) w.erase(w.begin());
            while (w.size()>0 && !isalpha(w.back())) w.erase(w.end()-1);
            if (w.size()==0) continue;
            // cout << w << endl;
            if (ban.find(w)==ban.end()) ++cnt[w];
        }

        string ans; int mx = 0;
        FOREACH(&kv, cnt)
            if (kv.second>mx) {
                mx = kv.second;
                ans = kv.first;
            }
        return ans;
    }

};