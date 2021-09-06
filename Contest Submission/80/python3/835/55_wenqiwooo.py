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
        node = head
        count = 0
        curr = 0
        while node is not None:
            if node.val in G:
                if curr == 0:
                    count += 1
                curr += 1
            else:
                curr = 0
            node = node.next
        return count
    