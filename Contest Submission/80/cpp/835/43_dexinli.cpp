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
        unordered_set<int> H{G.begin(),G.end()};
        int res = 0;
        auto p = head;
        bool flag = false;
        while(p!=nullptr) {
            if(H.count(p->val)) {
                flag = true;
            } else if(flag) {
                flag = false;
                res+=1;
            }
            p=p->next;
        }
        if(flag) {
            res+=1;
        }
        return res;
    }
};