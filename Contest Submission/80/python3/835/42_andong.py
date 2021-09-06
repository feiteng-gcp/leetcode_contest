# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        G = set(G)
        cnt = 0
        started = False
        while head.next:
            start = head.val
            end = head.next.val
            if start in G and end in G:
                if not started:
                    started = True
            else:
                if started:
                    started = False
                    cnt += 1
                elif head.val in G:
                    cnt += 1
            head = head.next
        if started or head.val in G:
            cnt += 1
        return cnt