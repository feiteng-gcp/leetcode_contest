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
        sort(G.begin(), G.end());
        
        int blockcount = 0;
        int currentstat = 0;
        
        while (head != NULL)
        {
            int l = 0;
            int r = G.size();
            int m = (l + r) / 2;
            bool isFound = false;
            int val = head->val;
            
            while (l < r)
            {
                //cout << val << ':' << l << ' ' << r << ' ' << m << endl;
                
                if (G[m] == val)
                {
                    isFound = true;
                    break;
                }
                else if (G[m] < val)
                {
                    l = m + 1;
                }
                else
                {
                    r = m;
                }
                
                m = (l + r) / 2;
            }
            
            if (G[m] == val)
                isFound = true;
            
            if (isFound)
            {
                //cout << "Found : " << val << endl;
                currentstat++;
                
                if (currentstat == 1)
                    blockcount++;
            }
            else
            {
                //cout << "No Found : " << val << endl;
                currentstat = 0;
            }
            
            head = head->next;
        }
        
        return blockcount;
    }
};