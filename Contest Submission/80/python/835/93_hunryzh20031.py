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
        g_set = set(G)
        p = head
        c = 0
        while p:
            q = p
            while q and q.val not in g_set:
                q = q.next
            if q:
                c += 1
                while q and q.val in g_set:
                    q = q.next
            p = q
        return c
        