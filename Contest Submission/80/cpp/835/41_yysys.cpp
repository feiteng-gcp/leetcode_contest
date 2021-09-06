/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

int flag[10005];
//int *flag = new int[10005];
class Solution {
public:
    
    int numComponents(ListNode* head, vector<int>& G) {
        
        for (int i = 0; i <= 10000; i++) flag[i] = 0;
        
        for (int i = 0; i < G.size(); i++) flag[G[i]] = 1;
        
        ListNode *now = head;
        
        while (now) {
            if (flag[now->val] == 1) {
                break;
            }
            now = now->next;
        }
        
        if (now == NULL) {
            return 0;
        }
        
        int ans = 0;
        int t = 1;
        while (now) {
            if (flag[now->val] == 0) {
                ans += t;
                t = 0;
            }
            else {
                t = 1;
            }
            now = now->next;
        }
        
        ans += t;
        
        return ans;
    }
};