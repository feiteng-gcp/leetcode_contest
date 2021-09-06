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
        int n=G.size();
	set<int> s;
	for(int i=0;i<n;i++)
	{
		s.insert(G[i]);
	}
	int ans=0,now=0;
	ListNode *p=head;
	while(p!=NULL)
	{
		if(s.find(p->val)==s.end())
		{
			if(now)ans++;
			now=0;
		}
		else now++;
		p=p->next;
	}
	if(now)ans++;
	return ans;
    }
};