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
        table = {k: True for k in G}
        
        node = head
        res = 0
        cur = False
        
        while node:
            if node.val in table:
                if cur:
                    pass
                else:
                    res += 1
                    cur = True
            else:
                if cur:
                    cur = False
                else:
                    pass
            node = node.next
        return res
        