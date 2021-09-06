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
        unordered_map<int, bool> s;
        for (auto i: G) s[i] = true;
        
        int sol = 0;
        int sz = 0;
        while (head) {
            int v = head->val;
            if (s.find(v) == s.end()) {
                if (sz) {
                    sz = 0;
                    sol++;
                }
            } else {
                sz++;
            }
            head = head->next;
        }
        if (sz) sol++;
        return sol;
    }   
};