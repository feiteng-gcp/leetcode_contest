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
        map<int,bool> mp;
        for(int i = 0;i < G.size();i++)
            mp[G[i]] = true;
        ListNode * now = head;
        bool flag = 0;
        int cnt = 0;
        if(mp.count(head->val))
            flag = 1,cnt++;
        
        while(now->next != NULL){
            bool f = 0;
            ListNode * nxt = now->next;
            if(mp.count(nxt->val)){
                f = 1;
            }
            if(!flag && f){
                cnt++;
            }
            flag = f;
            now = nxt;
        }
        return cnt;
    }
};