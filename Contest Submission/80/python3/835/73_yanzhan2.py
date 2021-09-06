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
        current = head
        G = set(G)
        exist = False
        count = 0
        while current:
            if current.val in G:
                exist = True
            else:
                if exist:
                    count += 1
                exist = False
            current = current.next
        if exist:
            count += 1
        return count