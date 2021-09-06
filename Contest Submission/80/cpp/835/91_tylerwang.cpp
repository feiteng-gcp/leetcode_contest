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
    unordered_set<int> g(G.begin(), G.end());
    int ans = 0, cur = 0;
    for (ListNode* i = head; i; i = i->next) {
      if (g.find(i->val) != g.end()) {
        ++cur;
      } else if (cur) {
        ++ans;
        cur = 0;
      }
    }
    if (cur) {
      ++ans;
    }
    return ans;
  }
};