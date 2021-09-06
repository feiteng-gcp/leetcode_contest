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
        
        vector<bool> contains(10100);
        for(int x : G)
            contains[x] = true;
        
        int ans = 0;
        for(ListNode *aux = head; aux != NULL; ) {
            
            if(contains[aux->val]) {
                ++ans;
                while(aux != NULL && contains[aux->val])
                    aux = aux->next;
            }
            else
                aux = aux->next;
        }
        
        return ans;   
    }
};