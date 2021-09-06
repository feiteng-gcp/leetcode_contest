typedef long long ll;
typedef vector<int> VI;
typedef pair<int,int> PII;

#define REP(i,s,t) for(int i=(s);i<(t);i++)
#define FILL(x,v) memset(x,v,sizeof(x))

const int INF = (int)1E9;
#define MAXN 100005

class Solution {
public:
  int numComponents(ListNode* head, vector<int>& G) {
    set<int> vals;
    REP(i,0,G.size()) vals.insert(G[i]);
    ListNode* now = head;
    VI uni;
    while (now != NULL) {
      if (vals.find(now->val) != vals.end()) uni.push_back(1);
      else uni.push_back(0);
      now = now->next;
    }
    uni.erase(unique(uni.begin(), uni.end()), uni.end());
    int ans = 0;
    REP(i,0,uni.size()) ans += uni[i];
    return ans;
  }
};