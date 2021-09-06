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
        
        unordered_set<int> setG;
        for (int i = 0; i < G.size(); ++i)
            setG.insert(G[i]);
        
        int count = 0;
        int len   = 0;        
        for (ListNode* pNode = head; pNode != NULL; pNode = pNode->next)
        {           
            if ( setG.find(pNode->val) != setG.end() ) ++len;
                
            if ( setG.find(pNode->val) == setG.end() ) len = 0;
                
            if (len == 1) ++count;            
        }
        
        return count;
    }
};