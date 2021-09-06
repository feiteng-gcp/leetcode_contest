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
        unordered_set<int> usets(G.begin(),G.end());
        int res = 0;
        int resTemp = 0;
        ListNode* node = head;
        
        while(node!=NULL)
        {
            if(usets.count(node->val)>0)
            {
                resTemp++;
            }
            else
            {
                if(resTemp>0)
                {
                    res++;
                }
                resTemp = 0;
            }
            node = node->next;
        }
        
        if(resTemp>0)
        {
            res++;
        }
        
        return res;
    }
};