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
        for (int i = 0; i < G.length; i++) set.add(G[i]);
        int result = 0;
        boolean isValueFound = false;
        while (head != null) {
            if (set.contains(head.val)) isValueFound = true;
            else {
                if (isValueFound) result++;
                isValueFound = false;
            }
            head = head.next;
        }
        if (isValueFound) result++;
        return result;
    }
}