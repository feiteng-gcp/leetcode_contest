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
        for(int i : G){
            set.add(i);
        }
        int size = 0;
        ListNode countCurr = head;
        while(countCurr != null){
            size++;
            countCurr = countCurr.next;
        }
        int[] roots = new int[size];
        for(int i = 0; i < roots.length; i++){
            roots[i] = i;
        }
        ListNode prev = null;
        ListNode curr = head;
        while(curr != null){
            if(prev != null && set.contains(prev.val) && set.contains(curr.val)){
                int rootA = roots[prev.val];
                int rootB = roots[curr.val];
                while(rootA != roots[rootA]) rootA = roots[rootA];
                while(rootB != roots[rootB]) rootB = roots[rootB];
                roots[rootA] = rootB;
            }
            prev = curr;
            curr = curr.next;
        }
        Set<Integer> comp = new HashSet<>();
        for(int i = 0; i < roots.length; i++){
            if(set.contains(i)){
                int root = i;
                while(root != roots[root]) root = roots[root];
                comp.add(root);
            }
        }
        return comp.size();
    }
}