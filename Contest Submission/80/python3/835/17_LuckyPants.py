# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        
        xxx = set()
        n = head
        while n:
            xxx.add(n.val)
            n = n.next
        G = set(G)&xxx
        
        x = False
        node = head
        ret = 0
        while node:
            if node.val in G:
                G.remove(node.val)
                ret += 1
                while node.next and node.next.val in G:
                    G.remove(node.next.val)
                    node = node.next
            node = node.next
        return ret