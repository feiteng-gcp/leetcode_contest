/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
public class Solution
{
    public int NumComponents(ListNode head, int[] G)
    {
        var value = new HashSet<int>();
        var root = new HashSet<int>();
        
        foreach(var g in G)
        {
            root.Add(g);
            value.Add(g);
        }
        
        while(head?.next != null)
        {
            if(value.Contains(head.val) && value.Contains(head.next.val))
            {
                if(root.Contains(head.next.val))
                {
                    root.Remove(head.val);
                }
            }
            head = head.next;
        }
        return root.Count();
    }
}