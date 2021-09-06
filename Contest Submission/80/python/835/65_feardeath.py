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
        indices = {x:0 for x in G}
        cur = head
        i = 0
        while cur is not None:
            if cur.val in indices:
                indices[cur.val] = i
            i += 1
            cur = cur.next
        l = sorted([indices[x] for x in indices])
        count = 1
        cur = l[0]
        for x in l[1:]:
            if x > cur+1:
                count += 1
            cur = x
        return count
        