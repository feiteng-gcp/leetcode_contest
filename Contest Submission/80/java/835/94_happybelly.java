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
        boolean[] has = new boolean[10010];
        int[] ps = new int[10010];
        int sz = 0;
        while (head != null) {
            ps[head.val] = sz++;
            head = head.next;
        }
        for (int n : G) {
            int p = ps[n];
            has[p] = true;
        }
        int ans = 0;
        for (int i = 0; i < has.length; i++)
            if (has[i] && (i == 0 || !has[i - 1])) ans++;
        return ans;
    }
}