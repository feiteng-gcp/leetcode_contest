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
        int result = 0;
        bool prevHit = false;
        set<int> setG;
        for (int i = 0; i < G.size(); i++) {
            setG.insert(G[i]);
        }
        while (head != nullptr) {
            bool hit = !(setG.find(head->val) == setG.end());
            if (hit && !prevHit) {
                result++;
            }
            prevHit = hit;
            head = head->next;
        }
        return result;
    }
};