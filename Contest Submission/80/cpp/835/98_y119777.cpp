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
int numComponents(ListNode* head, vector<int>& a) {
    set<int> se;
    for (int x : a)
        se.insert(x);
    int r = 0;
    while(head) {
        while(head && !se.count(head->val)) {
            head = head->next;
        }
        if(!head) break;
        while(head && se.count(head->val)) {
            head = head->next;
        }
        r++;
        while(head && !se.count(head->val)) {
            head = head->next;
        }
    }
    return r;
}
};