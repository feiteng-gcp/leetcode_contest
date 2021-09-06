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
        Set<Integer> set = new HashSet<>();
        for(int num : G) {
            set.add(num);
        }
        int res = 0;
        boolean inConnect = false;
        while(head!=null) {
            if(!set.contains(head.val)) {
                if(inConnect) {
                    inConnect = false;
                }
            } else {
                if(!inConnect) {
                    inConnect = true;
                    res++;
                }
            }
            head = head.next;
        }
        return res;
    }
}