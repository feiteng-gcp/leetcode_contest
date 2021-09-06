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
        map<int, bool> exist;
        for (const int &v: G) {
            exist[v] = true;
        }
        bool component = false;
        int answer = 0;
        ListNode *cur = head;
        while(cur) {
            if (exist[cur->val]) {
                component = true;
            } else if (component) {
                component = false;
                answer ++;
            }
            cur = cur->next;
        }
        if (component) {
            answer ++;
        }
        return answer;
    }
};
