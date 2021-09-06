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
        set<int> tab;
    int len = (int)G.size(), ans = 0;
    for(int i = 0; i < len; i++) tab.insert(G[i]);
    
    while(head)
    {
        if(tab.count(head->val) && (!head->next || !tab.count(head->next->val))) ans++;
        head = head->next;
    }
    return ans;
    }
};