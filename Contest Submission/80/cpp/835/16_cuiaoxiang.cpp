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
    int numComponents(ListNode* A, vector<int>& G) {
        map<int, int> idx;
        int k = 0;
        for (ListNode* p = A; p; p = p->next) {
            idx[p->val] = k++;
        }
        for (auto& it : G) {
            it = idx[it];
        }
        sort(G.begin(), G.end());
        int ret = 0;
        for (int i = 0, j; i < G.size(); i = j) {
            for (j = i + 1; j < G.size() && G[j] == G[j - 1] + 1; ++j);
            ++ret;
        }
        return ret;
        
    }
};