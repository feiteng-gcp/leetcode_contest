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
        unordered_set<int> table;
        for (int num : G) table.insert(num);
        bool in = false;
        int cnt = 0;
        while (head != NULL) {
            auto it = table.find(head->val);
            if (it == table.end() && in) {
                in = false;
            }
            else if (it != table.end() && !in) {
                cnt++;
                in = true;
            }
            head = head->next;
        }
        return cnt;
        
    }
};