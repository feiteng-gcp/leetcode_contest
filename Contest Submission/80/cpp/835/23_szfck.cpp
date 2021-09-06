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
    int numComponents(ListNode* head, vector<int>& G) {
        set<int> vis(G.begin(), G.end());
        int res = 0;
        ListNode* p  = head;
        int cnt = 0;
        while (p != nullptr) {
            if (vis.find(p->val) != vis.end()) {
                cnt++;
            } else {
                if (cnt > 0) {
                    res++;
                }
                cnt = 0;
            }
            p = p->next;
        }
        
        if (cnt > 0) {
            res++;
        }
        return res;
        
    }
};