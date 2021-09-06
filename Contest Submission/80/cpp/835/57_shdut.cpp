/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
#include<bits/stdc++.h>
class Solution {
public:
    int numComponents(ListNode* head, vector<int>& G) {
        map<int,int>g;
        for(auto &x:G)g[x]=1;
        int ans=0,flag=0;
        while(head!=NULL){
            int v=head->val;
            if(!g.count(v)){
                flag=0;
            }
            else{
                if(flag==0)ans++;
                flag=1;                
            }
            head=head->next;
        }
        return ans;
    }
};