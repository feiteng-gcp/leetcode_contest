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
    	Set<Integer> GSet = new HashSet<Integer>();
    	for(int i : G)
    		GSet.add(i);
    	int ans = 0;
    	int currentCombo = 0;
    	while(head != null) {
    		int n = head.val;
    		if(GSet.contains(n)) {
    			if(currentCombo == 0)
    				ans++;
    			currentCombo++;
    		} else {
    			currentCombo = 0;
    		}
    		head = head.next;
    	}
    	return ans;
    }
}