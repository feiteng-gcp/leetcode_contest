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
        for (int i = 0; i < G.length; i++) {
            set.add(G[i]);
        }
        
        int res = 0;
        while (head != null) {
            if (!set.contains(head.val)) {
                head = head.next;
                continue;
            }
            ListNode  cur = head;
            while (cur != null && set.contains(cur.val)) {
                cur = cur.next;
            }
            
            res++;
            head = cur;
        }
        return res;
    }
}