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
    int numComponents(ListNode* head, vector<int>& g) {
        unordered_set<int> dict;
        for (auto cur : g) dict.insert(cur);
        auto cur = head;
        int result = 0;
        bool is_in = false;
        while (cur) {
            if (is_in) {
                if (dict.count(cur->val) == 0) {
                    is_in = false;
                }
            } else {
                if (dict.count(cur->val) != 0) {
                    is_in = true;
                    result++;
                }
            }
            cur = cur->next;
        }
        return result;
    }
};