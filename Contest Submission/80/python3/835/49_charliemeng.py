# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from collections import defaultdict

class Solution:
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """

        mp = defaultdict(list)
        while head and head.next:
            mp[head.val].append(head.next.val)
            mp[head.next.val].append(head.val)
            head = head.next
        to_visit = set(G)
        res = 0
        for i in G:
            if i in to_visit:
                res += 1
                self.helper(i, mp, to_visit)
        return res

    def helper(self, i, mp, to_visit):
        to_visit.remove(i)
        for j in mp[i]:
            if j in to_visit:
                self.helper(j, mp, to_visit)