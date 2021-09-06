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
        set<int> st(G.begin(), G.end());
        int res = 0, flag = false;
        while (head != NULL) {
            if (st.find(head->val) != st.end()) {
                if (!flag) {
                    flag = true;
                    res++;
                }
            } else {
                flag = false;
            }
            head = head->next;
        }
        return res;
    }
};