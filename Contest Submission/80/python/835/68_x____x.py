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
        g = set(G)
        ret = 0
        sz = 0
        while head:
            if head.val in g:
                sz += 1
            else:
                if sz:
                    ret += 1
                    sz = 0
            head = head.next
        if sz:
            ret += 1
        return ret
    