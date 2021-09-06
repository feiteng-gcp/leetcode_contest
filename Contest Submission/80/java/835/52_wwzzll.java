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
        HashSet<Integer> target = new HashSet();
        for (int g : G) {
            target.add(g);
        }
        int count = 0;
        int tmpCount = 0;
        while(head != null) {
            if (target.contains(head.val)) {
                tmpCount++;
            } else {
                if (tmpCount > 0) {
                    tmpCount = 0;
                    count++;
                }
            }
            head = head.next;
        }
        if (tmpCount > 0) {
            count++;
        }
        return count;
    }
}