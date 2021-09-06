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
        vector<int>v;
        
        while(head!=NULL){
            v.push_back(head->val);
            head=head->next;
        }
        
        map<int,int>m;
        for(int i=0;i<G.size();i++)
            m[G[i]]=-1;
        
        int cont=0;
        bool sec=0;
        
        for(int i=0;i+1<v.size();i++){
            int a=v[i];
            int b=v[i+1];
            
            if(m.find(a)!=m.end() && m.find(b)!=m.end()){
                m[a]=cont;
                m[b]=cont;
            }else{
                cont++;
            }
        }
     
        vector<pair<int,int> >x(m.begin(),m.end());
        set<int>S;
        int dev=0;
        
        for(int i=0;i<x.size();i++){
            if(x[i].second==-1){
                dev++;
            }else{
                S.insert(x[i].second);
            }
            
        }
        
        dev+=S.size();
        return dev;
    }
};