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
        unordered_set<int> hash;
        
        for( int i = 0 ; i <G.size() ; ++i ) hash.insert(G[i]);
        
        ListNode* current = head;
        int lastVal = -1;
        int result = 0;
        while( current != NULL ){            
            /*if( lastVal == -1 ){
                lastVal = current -> val;
            }else{
                if( hash.find( current -> val ) != hash.end() ){
                    
                }
            }*/
            if( hash.find( current -> val ) != hash.end() ){
                result++;
                while( current != NULL && hash.find( current -> val ) != hash.end() ){
                    current = current -> next;
                }
            }else current = current -> next;
        }
        return result;
        
    }
};