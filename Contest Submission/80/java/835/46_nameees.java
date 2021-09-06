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
        HashMap<Integer, Integer> map = new HashMap<>();

        // map value to index
        ListNode cur = head;
        int index = 0;
        while (cur != null) {
            map.put(cur.val, index);
            // update
            cur = cur.next;
            index++;
        }

        // change value to index
        for (int i = 0; i < G.length; i++) {
            G[i] = map.get(G[i]);
        }

        // sort
        Arrays.sort(G);

        // count
        int count = 1;
        for (int i = 1; i < G.length; i++) {
            if (G[i] != G[i - 1] + 1) {
                count++;
            }
        }

        return count;

    }
}