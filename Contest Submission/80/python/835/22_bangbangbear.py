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
        
        prev_inG = False
        res = 0
        p = head
        while p != None:
            if p.val in G:
                if not prev_inG:
                    res += 1
                prev_inG = True
            else:
                prev_inG = False
            p = p.next
        
        return res
        