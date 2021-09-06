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
        m = {}
        pre = None
        n = head
        s = set(G)
        while n:
            if n.val in s:
                if pre is None:
                    m[n.val] = n.val
                else:
                    m[n.val] = m[pre.val]
                pre = n
            else:
                pre = None
            n = n.next
        ans = 0
        for key in m.keys():
            if m[key] == key:
                ans += 1
        return ans