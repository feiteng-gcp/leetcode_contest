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
        if (head == NULL) return 0;
        
        unordered_set<int> gset(G.begin(), G.end());
        
        int counter = 0;
        ListNode *cur,*next;
        cur = head;
        while (cur != NULL) {
            next = cur;
            auto it = gset.find(next->val);
            if (it != gset.end()) {
                ++counter;
                next = next->next;
                while (next != NULL) {
                    it = gset.find(next->val);
                    if (it == gset.end()) break;
                    next = next->next;
                }
            }
            cur = next;
            if (cur != NULL) cur = cur->next;
        }
        return counter;
    }
};