# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        G = set(G)
        s = False
        node = head
        r = 0
        while node:
            if node.val in G:
                if not s: s = True
            else:
                if s: r += 1
                s = False
            node = node.next
        if s: r += 1
        return r