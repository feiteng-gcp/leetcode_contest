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
        Set<Integer> gSet = new HashSet<>();
        for (int i : G) {
            gSet.add(i);
        }
        
        boolean hasGroup = false;
        int count = 0;
        while (head != null) {
            if (gSet.contains(head.val)) {
                hasGroup = true;
            } else {
                if (hasGroup) {
                    hasGroup = false;
                    count++;
                }
            }
            head = head.next;
        }
        if (hasGroup) count++;
        return count;
    }
}