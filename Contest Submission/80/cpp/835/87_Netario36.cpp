/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
private:
    int f[10005];
    
    int getFather(int x){
        if (f[x] != x) f[x] = getFather(f[x]);
        return f[x];
    }
    
public:
    int numComponents(ListNode* head, vector<int>& G) {
        unordered_set<int> hash;
        for (int i = 0; i < 10005; ++ i)
            f[i] = i;
        for (auto& x : G)
            hash.insert(x);
        ListNode *u = head;
        while (u != nullptr){
            if (u->next){
                if (hash.count(u->val) > 0 && hash.count(u->next->val) > 0){
                    f[getFather(u->val)] = getFather(u->next->val);
                }
            }
            u = u->next;
        }
        unordered_set<int> ans;
        for (auto& x : G){
            ans.insert(getFather(x));
            //cout << x << ' ' << getFather(x) << endl;
        }
        return ans.size();
    }
};