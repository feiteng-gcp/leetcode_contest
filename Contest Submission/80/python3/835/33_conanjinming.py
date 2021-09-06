# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import collections

class Solution:
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        c = collections.Counter()
        for val in G:
            c[val] += 1
        ans = 0
        cur = head
        con = 0
        while cur is not None:
            if c[cur.val] == 0 and con == 1:
                con = 0
            elif c[cur.val] > 0 and con == 0:
                con = 1
                ans += 1
            cur = cur.next
        return ans