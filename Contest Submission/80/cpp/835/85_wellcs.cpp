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
        set<int> s(G.begin(), G.end());
        int len = 0;
        int ret = 0;
        ListNode* cur = head;
        while(cur != NULL)
        {
            if(s.count(cur->val) != 0)
            {
                len++;
            }
            else
            {
                if(len > 0)
                {
                    ret++;
                }
                
                len = 0;
            }
            
            cur = cur->next;
        }
        
        if(len > 0)
        {
            ret++;
        }
        
        return ret;
    }
};