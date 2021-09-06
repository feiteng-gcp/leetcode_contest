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
        set<int> ng;
        for (int i = 0; i < G.size(); i++) {
            ng.insert(G[i]);
        }
        
        int total = 0;
        bool prev = false;
        while (head) {
            if (ng.count(head->val) > 0) {
                prev = true;
            } else {
                if (prev) total++;
                prev = false;
            }
            
            head = head->next;
        }
        if (prev) total++;
        
        return total;
    }
};