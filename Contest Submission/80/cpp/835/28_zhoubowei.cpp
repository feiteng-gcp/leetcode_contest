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
        int len = 0;
        ListNode* h = head;
        while (h) {
            len++;
            h = h->next;
        }
        vector<int> v(len);
        h = head;
        int i = 0;
        while (h) {
            v[h->val] = i;
            h = h->next;
            i++;
        }
        
        for (auto& g : G) g = v[g];
        sort(G.begin(), G.end());
        
        int last = -2;
        int result = 0;
        for (auto g : G) {
            // cout << g << last+1 << endl;
            if (g != last + 1) {
                result++;
            }
            last = g;
        }
        return result;
    }
};