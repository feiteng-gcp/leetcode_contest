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
        unordered_map<int,int> val2pos;
        unordered_map<int,int> pos2val;
        ListNode* cur = head;
        int i = 0;
        while (cur != NULL) {
            val2pos[cur->val] = i;
            pos2val[i] = cur->val;
            ++i;
            cur = cur->next;
        }
        int n = val2pos.size();

        unordered_set<int> s;
        for (auto num : G) {
            s.insert(num);
        }
        
        int res = 0;
        while (!s.empty()) {
            auto it = s.begin();
            int num = *it;
            s.erase(it);
            if (val2pos.count(num) == 0) {
                continue;
            }
            ++res;
            int pos = val2pos[num];
            int i = pos - 1;
            while (i >= 0) {
                num = pos2val[i];
                if (s.count(num) > 0) {
                    s.erase(num);
                } else {
                    break;
                }
                --i;
            }
            i = pos + 1;
            while (i < n) {
                num = pos2val[i];
                if (s.count(num) > 0) {
                    s.erase(num);
                } else {
                    break;
                }
                ++i;
            }
        }
        
        return res;
    }
};