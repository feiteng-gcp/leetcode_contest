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
    int numComponents(ListNode* u, vector<int>& g) {
        unordered_set<int> subset;
        for(int x : g){
            subset.insert(x);
        }
        
        int cum = 0;
        bool on = false;
        
        
        while(u != nullptr){
            if(subset.count(u->val)){
                if(!on) on = true, cum++;
            } else {
                on = false;
            }
            
            u = u->next;
        }
        
        return cum;
    }
};