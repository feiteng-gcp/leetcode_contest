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
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    unordered_map<int, int> fa;

    int find(int x) {
        return fa[x]==x ? x : fa[x]=find(fa[x]);
    }

  void link(int x, int y) {
    int fx = find(x), fy = find(y);
    fa[fx] = fy;
  }

    int numComponents(ListNode* head, vector<int>& G) {
        FOREACH(x, G) fa[x] = x;

        ListNode* fst = new ListNode(0); fst->next = head;
        for (auto it = fst->next, iit = head->next;
                     it && iit; iit=iit->next, it=it->next) {
            if (fa.find(it->val)!=fa.end() && fa.find(iit->val)!=fa.end())
                link(it->val, iit->val);
        }
        int cmp = 0;
        FOREACH(&kv, fa)
            if (kv.first==find(kv.second))
                ++cmp;
        return cmp;
    }
};