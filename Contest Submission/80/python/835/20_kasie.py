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
        isv = {}
        p = head
        while p:
            isv[p.val] = False
            p = p.next
        for v in G:
            isv[v] = True
        ans = 0
        q = None
        p = head
        while p:
            if isv[p.val] and (not q or not isv[q.val]): ans += 1
            q = p
            p = p.next
        return ans