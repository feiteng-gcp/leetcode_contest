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
        for (int n : G) {
            set.add(n);
        }
        int count = 0;
        int len = 0;
        ListNode curr = head;
        while (curr != null) {
            if (set.contains(curr.val)) {
                len++;
            } else if (len > 0) {
                count++;
                len = 0;
            }
            curr = curr.next;
        }
        if (len > 0) {
            count++;
        }
        return count;
    }
}