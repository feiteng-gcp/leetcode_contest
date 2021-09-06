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
        unordered_set<int> values;
        for(auto g : G) values.insert(g);
        int components = 0, prev = -1;
        while(head != NULL) {
            if (!values.count(head->val) && values.count(prev)) {
                components++;
            }
            prev = head->val;
            head = head->next;
        }
        components += values.count(prev);
        return components;
    }
};