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

    vector<string> solve(string s) {
        vector<string> ans;
        if (s.empty()) return {};

        if (s[0]!='0' || s.size()==1) ans.PB(s); // not start with 0
        int n = s.size();

        REP(i, 0, n-2) {
            string a = s.substr(0, i+1), b = s.substr(i+1);
            if ((a[0]!='0' || a.size()==1) && b.back()!='0')
                ans.PB(a+"."+b);
        }

        return ans;
    }

    vector<string> ambiguousCoordinates(string s) {
        s.erase(s.begin()), s.erase(s.end()-1);
        int n = s.size();
        vector<string> ans;
        REP(i, 0, n-2) 
            FOREACH(&x, solve(s.substr(0, i+1)))
                FOREACH(&y, solve(s.substr(i+1)))
                    ans.PB("("+x+", "+y+")");

        return ans;
    }

};