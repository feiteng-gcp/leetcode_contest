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
        set<int> st(G.begin(), G.end());
        int cnt = 0;
        bool in_set = false;
        while(head != NULL){
            if(st.count(head->val)){
                if(!in_set){
                    in_set = true;
                    ++cnt;
                }
            }else{
                in_set = false;
            }
            
            head = head->next;
        }
        
        return cnt;
    }
};