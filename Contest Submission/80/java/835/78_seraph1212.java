/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    int find(int x, Map<Integer, Integer> u) {
        int par = u.getOrDefault(x, -1);
        if (par == -1 || par == x) return par;
        int pp = find(par, u);
        u.put(x, pp);
        return pp;
    }
    void merge(int a, int b, Map<Integer, Integer> u) {
        if (a == b) return;
        int aa = find(a, u);
        int bb = find(b, u);
        if (aa == -1 || bb == -1 || aa == bb) return;
        u.put(aa, bb);
    }
    public int numComponents(ListNode head, int[] G) {
        Map<Integer, Integer> u = new HashMap<>();
        for (int i : G) {
            u.put(i, i);
        }
        for (ListNode node = head; node.next != null; node = node.next) {
            merge(node.val, node.next.val, u);
        }
        Set<Integer> con = new HashSet<>();
        for (int i : G) con.add(find(i, u));
        return con.size();
    }
}