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
        Set<Integer> sub = new HashSet<>();
        for(int val : G) {
            sub.add(val);
        }
        
        int ans = 0; boolean connected = false;
        while(head != null) {
            int val = head.val;
            if(sub.contains(val)) {
                if(!connected) {
                    ans++;
                    connected = true;
                }
            } else {
                connected = false;
            }
            
            head = head.next;
        }
        return ans;
    }
}