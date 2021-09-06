/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public int numComponents(ListNode head, int[] G) {
        int n=G.length;
        Set<Integer> set=new HashSet<>();
        for(int i: G) set.add(i);
        //boolean[] visit=new boolean[n];
        
        int count=0;
        while(head!=null){
            if(!set.contains(head.val)){
                head=head.next;
            }
            else{
                count++;
                while(head!=null&&set.contains(head.val)){
                    head=head.next;
                }
            }
        }
        
        return count;
    }
}