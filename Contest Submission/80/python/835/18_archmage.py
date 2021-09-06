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
        p = head
        t = 0
        vals = dict()
        while p is not None:
            vals[p.val] = t
            t += 1
            p = p.next
        G2 = sorted(vals[x] for x in G)
        ans = 1
        for i in xrange(1, len(G2)):
            if G2[i] > G2[i-1] + 1:
                ans += 1
        return ans

