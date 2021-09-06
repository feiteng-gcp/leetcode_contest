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
        unordered_set<int> s;
        for (int i:G) s.insert(i);
        int res = 0;
        bool prev = false;
        ListNode *cur = head;
        while (cur != NULL) {
            if (s.find(cur->val) == s.end()) {
                if (prev) {
                    res += 1;
                    prev = false;
                }
            }
            else {
                if (!prev) prev = true;
            }
            cur = cur->next;
        }
        if (prev) res++;
        return res;
    }
};