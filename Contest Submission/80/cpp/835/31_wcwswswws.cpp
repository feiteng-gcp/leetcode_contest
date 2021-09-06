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
        int ans = 0;
        unordered_set<int> dict_set;
        for (const auto& iter : G) {
            dict_set.insert(iter);
        }
        bool last_in = false;
        while (head != nullptr) {
            if (dict_set.find(head->val) == dict_set.end()) {
                if (last_in) {
                    last_in = false;
                }
            } else {
                if (!last_in) {
                    ans++;
                    last_in = true;
                }
            }
            head = head->next;
        }
        return ans;
    }
};