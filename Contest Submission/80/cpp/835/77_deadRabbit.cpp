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
    int numComponents(ListNode* p, vector<int>& G) {
        int res = 0;
        set<int> A; for (int x : G) A.insert(x);
        while(p) {
            if (A.count(p->val)) {
                ++res;
                while(p && A.count(p->val)) p=p->next;
            } else p = p->next;
        }
        return res;
    }
};